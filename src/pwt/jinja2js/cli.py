import optparse
import os.path
import string
import sys

import soy_wsgi
import jscompiler

def main(args = None, output = None):
    if output is None:
        output = sys.stdout

    parser = optparse.OptionParser()
    # closure template options that we support
    parser.add_option("--outputPathFormat", dest = "output_format",
                      help = "A format string that specifies how to build the path to each output file.",
                      metavar = "OUTPUT_FORMAT")

    # jinja2js specific options
    parser.add_option("--packages", dest = "packages",
                      default = [], action = "append",
                      help = "List of packages to look for template files",
                      metavar = "PACKAGE")

    options, files = parser.parse_args(args)

    outputPathFormat = options.output_format
    if not outputPathFormat:
        parser.print_help(output)
        return 1

    env = soy_wsgi.create_environment(options.packages)

    filename_template = string.Template(options.output_format)

    for filename in files:
        name = os.path.basename(filename)
        node = env._parse(open(filename).read(), name, filename)

        output = jscompiler.generate(node, env, name, filename)

        output_filename = filename_template.substitute({
            "INPUT_FILE_NAME": os.path.basename(filename),
            "INPUT_FILE_NAME_NO_EXT": os.path.splitext(os.path.basename(filename))[0],
            "INPUT_DIRECTORY": os.path.dirname(filename),
            # "INPUT_PREFIX": 
            })
        open(output_filename, "w").write(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
