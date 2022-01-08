Import("env")
from os.path import join
from os import sep

pio_platform = env.PioPlatform()
# get absolute path of project source directory
src_dir = env.subst("$PROJECT_SRC_DIR")
# add include paths and linker flags
env.Append(
  CPPPATH=[
    join(src_dir, "ASF", "common", "boards"),
    join(src_dir, "ASF", "common", "boards", "user_board"),
    join(src_dir, "ASF", "common", "services", "clock"),
    join(src_dir, "ASF", "common", "services", "delay"),
    join(src_dir, "ASF", "common", "utils"),
    join(src_dir, "ASF", "sam", "drivers"),
    join(src_dir, "ASF", "sam", "drivers", "chipid"),
    join(src_dir, "ASF", "sam", "drivers", "efc"),
    join(src_dir, "ASF", "sam", "drivers", "matrix"),
    join(src_dir, "ASF", "sam", "drivers", "pio"),
    join(src_dir, "ASF", "sam", "drivers", "pmc"),
    join(src_dir, "ASF", "sam", "drivers", "pwm"),
    join(src_dir, "ASF", "sam", "drivers", "rstc"),
    join(src_dir, "ASF", "sam", "drivers", "uart"),
    join(src_dir, "ASF", "sam", "drivers", "wdt"),
    join(src_dir, "ASF", "sam", "services", "flash_efc"),
    join(src_dir, "ASF", "sam", "utils"),
    #join(src_dir, "ASF", "sam", "utils", "cmsis", "sam3s", "include"),
    #join(src_dir, "ASF", "sam", "utils", "cmsis", "sam3s", "source", "templates"),
    join(src_dir, "ASF", "sam", "utils", "cmsis", "sam4s", "include"),
    join(src_dir, "ASF", "sam", "utils", "cmsis", "sam4s", "source", "templates"),
    join(src_dir, "ASF", "sam", "utils", "header_files"),
    join(src_dir, "ASF", "sam", "utils", "preprocessor"),
    join(src_dir, "ASF", "thirdparty", "CMSIS", "Include"),
    join(src_dir, "UI"),
    join(src_dir, "config"),
  ],
  LINKFLAGS=[
    "--specs=nano.specs", 
    "-Wl,--defsym,__stack_size__=0x1000", 
    "-Wl,-Map,\"%s\"" %  join(env.subst("$PROJECT_BUILD_DIR"), env.subst("$PIOENV"), "paneldue.map")],
)

# link against libmath (implicit at the end), libc, libgcc
env.Replace(
   LIBS=["c", "gcc", "m", "stdc++"]
)

# set linkerscript
env.Append(LIBPATH=[join(src_dir, "ASF", "sam", "utils", "linker_scripts", "sam4s", "sam4s4", "gcc")])
env.Replace(LDSCRIPT_PATH ="flash.ld")
# add ARM Cortex M4 Math define
env.Append(CPPDEFINES= [("ARM_MATH_CM4", 1)])
# replace firmware name so that paneldue.elf is produced instead of firmware.elf
env.Replace(PROGNAME="paneldue")