#include <gtk/gtk.h>
#include <iostream>
#include <string>
#include <random>
#include <locale>
#include <codecvt>  // Include for converting between UTF-8 and wide strings

GtkWidget *entry_length, *entry_password, *window;
GtkCssProvider *css_provider;

// Function to generate a password
std::wstring generate_password(int length) {
    const wchar_t charset[] =
        L"абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        L"0123456789!@#$%^&*()";

    size_t charset_size = sizeof(charset) / sizeof(charset[0]) - 1; // Exclude null terminator

    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_int_distribution<size_t> distribution(0, charset_size - 1);

    std::wstring password;
    for (int i = 0; i < length; i++) {
        size_t index = distribution(generator);
        password += charset[index];

        // Debugging output to check generated characters
        std::wcout << L"Character generated: " << charset[index] << L" (index: " << index << L")" << std::endl;
    }
    return password;
}

// Callback function to handle password generation
void on_generate_password(GtkWidget *widget, gpointer data) {
    const char *len_text = gtk_entry_get_text(GTK_ENTRY(entry_length));
    try {
        int length = std::stoi(len_text);
        if (length <= 0) {
            throw std::invalid_argument("Length must be positive");
        }
        std::wstring password = generate_password(length);
        
        // Convert wstring to string for GTK entry
        std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
        std::string utf8_password = converter.to_bytes(password);
        gtk_entry_set_text(GTK_ENTRY(entry_password), utf8_password.c_str());
    } catch (std::invalid_argument&) {
        gtk_entry_set_text(GTK_ENTRY(entry_password), "Ошибка 1 - Недопустимая длина");
    } catch (std::out_of_range&) {
        gtk_entry_set_text(GTK_ENTRY(entry_password), "Ошибка 2 - Длина вне диапазона");
    }
}

// Function to copy the password to the clipboard
void on_copy_to_clipboard(GtkWidget *widget, gpointer data) {
    const char *password = gtk_entry_get_text(GTK_ENTRY(entry_password));
    GtkClipboard *clipboard = gtk_clipboard_get(GDK_SELECTION_CLIPBOARD);
    gtk_clipboard_set_text(clipboard, password, -1);
}

// Main function
int main(int argc, char *argv[]) {
    setlocale(LC_ALL, "ru_RU.UTF-8");  // Set locale to Russian UTF-8
    gtk_init(&argc, &argv);

    // Main window
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Генератор паролей!");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 250);
    gtk_window_set_resizable(GTK_WINDOW(window), FALSE);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), nullptr);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_set_border_width(GTK_CONTAINER(vbox), 15);
    gtk_container_add(GTK_CONTAINER(window), vbox);

    // Header
    GtkWidget *title = gtk_label_new("<u><b><big> Генератор паролей: </big></b></u>");
    gtk_label_set_use_markup(GTK_LABEL(title), TRUE);
    gtk_box_pack_start(GTK_BOX(vbox), title, FALSE, FALSE, 3);

    // Input field for password length
    GtkWidget *label_length = gtk_label_new("Введите длину пароля:");
    gtk_box_pack_start(GTK_BOX(vbox), label_length, FALSE, FALSE, 5);

    entry_length = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(entry_length), "Например - 12");
    gtk_box_pack_start(GTK_BOX(vbox), entry_length, FALSE, FALSE, 5);

    // Button to generate password
    GtkWidget *generate_button = gtk_button_new_with_label("Сгенерировать пароль");
    g_signal_connect(generate_button, "clicked", G_CALLBACK(on_generate_password), nullptr);
    gtk_box_pack_start(GTK_BOX(vbox), generate_button, FALSE, FALSE, 10);

    // Field to display the generated password
    entry_password = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(entry_password), "Сгенерированный пароль появится здесь");
    gtk_box_pack_start(GTK_BOX(vbox), entry_password, FALSE, FALSE, 5);

    // Button to copy to clipboard
    GtkWidget *copy_button = gtk_button_new_with_label("Копировать в буфер обмена");
    g_signal_connect(copy_button, "clicked", G_CALLBACK(on_copy_to_clipboard), nullptr);
    gtk_box_pack_start(GTK_BOX(vbox), copy_button, FALSE, FALSE, 5);

    // CSS for styling buttons, window, and input fields
    css_provider = gtk_css_provider_new();
    gtk_css_provider_load_from_data(css_provider,
        "window { background-color: #FFFFFF; color: #000000; }"
        "entry, label { color: #000000; padding: 5px; }"
        "entry { border-style: solid; border-width: 3px; border-color: #000000; border-radius: 5px; padding: 5px; }"
        "button { color: #000000; background-color: #C0C0C0; border-style: solid; border-width: 3px; border-color: #000000; border-radius: 5px; padding: 5px; }"
        "button:hover { background-color: #A0A0A0; }", -1, nullptr);
    gtk_style_context_add_provider_for_screen(gdk_screen_get_default(),
                                              GTK_STYLE_PROVIDER(css_provider),
                                              GTK_STYLE_PROVIDER_PRIORITY_USER);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}
