# MiniShell

MiniShell is a simple command line shell project written in C for an Operating Systems course. It displays a custom prompt, reads commands from the user, and executes supported system commands on Windows.

## Features

- Custom prompt: `mysh>`
- Runs continuously until the user types `exit`
- Executes commands using `system()`
- Supports common commands such as:
  - `ls` translated to `dir` on Windows
  - `pwd`
  - `cd`
  - `mkdir`
  - `clear` translated to `cls` on Windows
  - `cls`
  - `echo`
  - `exit`
- Handles empty input and invalid commands gracefully
- Organized using CMake

## Project Structure

```text
MiniShell/
|
+-- CMakeLists.txt
+-- README.md
+-- src/
|   +-- main.c
+-- build/
```

## Build Instructions

Open a terminal in the `MiniShell` folder and run:

```bash
cmake -S . -B build
cmake --build build
```

On Windows with Visual Studio generators, the executable is usually created in:

```text
build\Debug\minishell.exe
```

If you use MinGW or another single-configuration generator, it may be created in:

```text
build\minishell.exe
```

## Run Instructions

From the `MiniShell` folder, run one of the following commands depending on your build system:

```bash
build\Debug\minishell.exe
```

or:

```bash
build\minishell.exe
```

## Example Commands

```text
mysh> pwd
mysh> ls
mysh> mkdir test_folder
mysh> cd test_folder
mysh> echo Hello from MiniShell
mysh> clear
mysh> exit
```

## Notes

- The `cd` command is handled inside the program because changing directories with `system("cd ...")` would only affect the temporary command process, not MiniShell itself.
- On Windows, `ls` is translated to `dir`, and `clear` is translated to `cls`.
