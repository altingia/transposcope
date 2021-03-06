"""
File: transposcope_parser.py
Author: Mark Grivainis
Email: mark.grivainis@fenyolab.org
Github: https://github.com/MarkGrivainis
Description: Command line parser which runs relative TranspoScope
    functions
"""

import argparse

import transposcope.viewer.server as server
import transposcope.driver as ts


def main():
    """Description

    @param param:  Description
    @type  param:  Type

    @return:  Description
    @rtype :  Type

    @raise e:  Description
    """
    parser = argparse.ArgumentParser(
        prog="TranspoScope",
        description="A tool for visualizing mobile elements supporting"
        + "read coverage within a genome",
    )
    # TODO - add help for transposcope
    # TODO - set default for transposcope parser
    subparsers = parser.add_subparsers(dest="{align|view}")
    subparsers.required = True
    transposcope_parser = subparsers.add_parser(
        "align",
        help=(
            "Align performs a local realignment using reads flanking a"
            + " potential insertion site and a reference sequence which includes"
            + " the sequence for the mobile element"
        ),
    )
    transposcope_parser.add_argument(
        "index_type",
        type=str,
        help="The software used to identify insertions",
        choices=["melt", "tipseqhunter"],
    )
    transposcope_parser.add_argument(
        "index",
        type=str,
        help="The path to the index file which describes the coordinates of insertion sites",
    )
    transposcope_parser.add_argument("bam", type=str, help="path to bam file")
    transposcope_parser.add_argument(
        "me_reference", type=str, help="path to the mobile element's FASTA file",
    )
    transposcope_parser.add_argument(
        "host_reference",
        type=str,
        help="path to a folder containing all of the chromosome FASTA files for the host genome",
    )
    transposcope_parser.add_argument(
        "sample_id",
        type=str,
        help="Unique name to for the given experiment. This is used to label the output.",
    )
    transposcope_parser.add_argument(
        "--genes",
        type=str,
        help="Path to refFlat.txt (If information regarding the nearest gene should be included.)",
    )
    transposcope_parser.add_argument(
        "--group1",
        type=str,
        help="First level group tag (default: %(default)s)",
        default="ungrouped",
    )
    transposcope_parser.add_argument(
        "--group2",
        type=str,
        help="Second level group tag (default: %(default)s)",
        default="ungrouped",
    )

    transposcope_parser.add_argument(
        "--keep_files",
        help=(
            "Flag which determines whether intermediate bam files and"
            + " fasta files are deleted (default: %(default)s)"
        ),
        action="store_true",
    )

    transposcope_parser.set_defaults(func=ts.main)

    viewer_parser = subparsers.add_parser(
        "view", help="Launch a web page to view the aligned output."
    )
    viewer_parser.add_argument(
        "web_directory",
        type=str,
        help="The path to the web directory created by the align tool.",
    )
    viewer_parser.set_defaults(func=server.main)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
