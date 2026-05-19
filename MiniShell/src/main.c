#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <direct.h>

#define MAX_INPUT_SIZE 1024

void parse_input(char *input);
int command_matches(const char *command, const char *name);
void execute_command(const char *command);
void show_help(void);
void shell_loop(void);

void parse_input(char *input)
{
    size_t length;
    char *start;
    char *end;

    if (input == NULL) {
        return;
    }

    length = strlen(input);

    if (length > 0 && input[length - 1] == '\n') {
        input[length - 1] = '\0';
    }

    start = input;

    while (*start != '\0' && isspace((unsigned char)*start)) {
        start++;
    }

    if (start != input) {
        memmove(input, start, strlen(start) + 1);
    }

    if (input[0] == '\0') {
        return;
    }

    end = input + strlen(input) - 1;

    while (end >= input && isspace((unsigned char)*end)) {
        *end = '\0';
        end--;
    }
}

int command_matches(const char *command, const char *name)
{
    size_t name_length;

    if (command == NULL || name == NULL) {
        return 0;
    }

    name_length = strlen(name);

    return strncmp(command, name, name_length) == 0 &&
           (command[name_length] == '\0' ||
            isspace((unsigned char)command[name_length]));
}

void show_help(void)
{
    printf("\n");
    printf("========== MiniShell Commands ==========\n");
    printf("help        - Show available commands\n");
    printf("pwd         - Show current directory\n");
    printf("cd <dir>    - Change directory\n");
    printf("ls          - List files and folders\n");
    printf("mkdir <dir> - Create a new directory\n");
    printf("echo <text> - Print text\n");
    printf("clear       - Clear screen\n");
    printf("date        - Show current date\n");
    printf("time        - Show current time\n");
    printf("exit        - Exit shell\n");
    printf("========================================\n");
    printf("\n");
}

void execute_command(const char *command)
{
    int result;
    const char *path;
    char current_directory[MAX_INPUT_SIZE];
    char translated_command[MAX_INPUT_SIZE + 4];

    if (command == NULL || command[0] == '\0') {
        return;
    }

    if (strcmp(command, "help") == 0) {
        show_help();
        return;
    }

    if (strcmp(command, "exit") == 0) {
        return;
    }

    if (strcmp(command, "pwd") == 0) {

        if (_getcwd(current_directory,
                    sizeof(current_directory)) != NULL) {

            printf("%s\n", current_directory);

        } else {
            perror("pwd failed");
        }

        return;
    }

    if (command_matches(command, "cd")) {

        path = command + 2;

        while (*path != '\0' &&
               isspace((unsigned char)*path)) {

            path++;
        }

        if (*path == '\0') {
            printf("Usage: cd <directory>\n");
            return;
        }

        if (_chdir(path) != 0) {
            perror("cd failed");
        }

        return;
    }

    if (command_matches(command, "ls")) {

        snprintf(translated_command,
                 sizeof(translated_command),
                 "dir%s",
                 command + 2);

        result = system(translated_command);
    }

    else if (strcmp(command, "clear") == 0 ||
             strcmp(command, "cls") == 0) {

        result = system("cls");
    }

    else if (strcmp(command, "date") == 0) {

        result = system("date /t");
    }

    else if (strcmp(command, "time") == 0) {

        result = system("time /t");
    }

    else if (command_matches(command, "dir") ||
             command_matches(command, "mkdir") ||
             command_matches(command, "echo")) {

        result = system(command);
    }

    else {

        printf("Invalid or unsupported command: %s\n",
               command);

        return;
    }

    if (result != 0) {
        printf("Command execution returned code: %d\n",
               result);
    }
}

void shell_loop(void)
{
    char input[MAX_INPUT_SIZE];

    while (1) {

        printf("[MiniShell] > ");
        fflush(stdout);

        if (fgets(input,
                  sizeof(input),
                  stdin) == NULL) {

            printf("\n");
            break;
        }

        parse_input(input);

        if (input[0] == '\0') {
            continue;
        }

        if (strcmp(input, "exit") == 0) {

            printf("Exiting MiniShell...\n");
            break;
        }

        execute_command(input);
    }
}

int main(void)
{
    printf("====================================\n");
    printf("       Welcome to MiniShell\n");
    printf("====================================\n");
    printf("Type 'help' to see commands.\n\n");

    shell_loop();

    return 0;
}