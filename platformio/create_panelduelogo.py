from os.path import join
Import("env")

# create paneldue-logo.bin
def create_paneldue_logo(source, target, env):
    output_dir = env.subst("$PROJECT_BUILD_DIR")
    output_path = join(output_dir, env.subst("$PIOENV"), "paneldue-logo.bin")
    splashscreen_path = join(env.subst(
        "$PROJECT_SRC_DIR"), "..", "SplashScreens", "SplashScreen-Duet3D-800x480.bin")
    bin_path = str(target[0])
    print("Merging " + bin_path + " and " + splashscreen_path)
    print("Into " + output_path)
    # merge the two files in binary node
    out_data = b''
    with open(bin_path, 'rb') as fp:
        out_data += fp.read()
    with open(splashscreen_path, 'rb') as fp:
        out_data += fp.read()
    with open(output_path, 'wb') as fp:
        fp.write(out_data)

# hook post action for paneldue.bin to created paneldue-logo.bin
env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", create_paneldue_logo)