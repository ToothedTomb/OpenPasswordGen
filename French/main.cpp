// Adding libraries 
#include <gtk/gtk.h> // Add gtk library to make the gui program. Its a tool that allows you to create 
// GUIs in c++...
#include <iostream>
#include <string>
#include <sstream>
#include <random>

GtkWidget *entry_length, *entry_password, *window;
GtkCssProvider *css_provider;
//Set of strings in the english that will generate a password with those strings.  Its random as well.
std::string generate_password(int length) {
    const char charset[] =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_int_distribution<size_t> distribution(0, sizeof(charset) - 2);

    std::string password;
    for (int i = 0; i < length; i++)
        password += charset[distribution(generator)];
    return password;
}
//If successfully display a password if not display an error message.
void on_generate_password(GtkWidget *widget, gpointer data) {
    const char *len_text = gtk_entry_get_text(GTK_ENTRY(entry_length));
    try {
        int length = std::stoi(len_text);
        std::string password = generate_password(length);
        gtk_entry_set_text(GTK_ENTRY(entry_password), password.c_str());
    } catch (std::invalid_argument&) {
        gtk_entry_set_text(GTK_ENTRY(entry_password), "Erreur 1 - Taille invalide");
    } catch (std::out_of_range&) {
        gtk_entry_set_text(GTK_ENTRY(entry_password), "Erreur 2 - Taille trop grande");
    }
}
//This function will allow you to copy the password and pate it into any program. 
void on_copy_to_clipboard(GtkWidget *widget, gpointer data) {
    const char *password = gtk_entry_get_text(GTK_ENTRY(entry_password));
    GtkClipboard *clipboard = gtk_clipboard_get(GDK_SELECTION_CLIPBOARD);
    gtk_clipboard_set_text(clipboard, password, -1);
}
// The main function is the function that run first in this C++ Language. So here we have created the window.
int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    // Main Window
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Générateur de mot de passe Open Source");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 250);
    gtk_window_set_resizable(GTK_WINDOW(window), FALSE);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), nullptr);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_set_border_width(GTK_CONTAINER(vbox), 15);
    gtk_container_add(GTK_CONTAINER(window), vbox);

    // Title
    GtkWidget *title = gtk_label_new("<u><b><big> Générateur de mot de passe Open Source: </big></b></u>");
    gtk_label_set_use_markup(GTK_LABEL(title), TRUE);
    gtk_box_pack_start(GTK_BOX(vbox), title, FALSE, FALSE, 3);
    //Entry box to allow you to enter how long you want the password to be...
    GtkWidget *label_length = gtk_label_new("Entrer la taille du mot de passe:");
    gtk_box_pack_start(GTK_BOX(vbox), label_length, FALSE, FALSE, 5);

    entry_length = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(entry_length), "Exemple - 12");
    gtk_box_pack_start(GTK_BOX(vbox), entry_length, FALSE, FALSE, 5);
    // This button allows you to generate your password when you entered the number of strings. 
    GtkWidget *generate_button = gtk_button_new_with_label("Generate Password");
    g_signal_connect(generate_button, "clicked", G_CALLBACK(on_generate_password), nullptr);
    gtk_box_pack_start(GTK_BOX(vbox), generate_button, FALSE, FALSE, 10);
    //This is where you will see the generated password...
    entry_password = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(entry_password), "Le mot de passe généré apparaîtra ici!");
    gtk_box_pack_start(GTK_BOX(vbox), entry_password, FALSE, FALSE, 5);
    //With this button you will be able to copy to clipboard...
    GtkWidget *copy_button = gtk_button_new_with_label("Copier dans le presse papier");
    g_signal_connect(copy_button, "clicked", G_CALLBACK(on_copy_to_clipboard), nullptr);
    gtk_box_pack_start(GTK_BOX(vbox), copy_button, FALSE, FALSE, 5);

    // CSS Provider for style on the buttons window and entry. 
    css_provider = gtk_css_provider_new();
    gtk_css_provider_load_from_data(css_provider,
        "window { background-color: #FFFFFF; color: #000000; }"
        "entry, label { color: #000000; padding: 5px; }"
        "entry { border-style: solid; border-width: 3px; border-color: #000000; border-radius: 5px; padding: 5px; }"

        "button { color: #000000; background-color: #C0C0C0; border-style: solid; border-width: 3px; border-color: #000000; border-radius: 5px; padding: 5px; }"       
        "button:hover { background-color: #A0A0A0; }",-1, nullptr);
    gtk_style_context_add_provider_for_screen(gdk_screen_get_default(),
                                              GTK_STYLE_PROVIDER(css_provider),
                                              GTK_STYLE_PROVIDER_PRIORITY_USER);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}
