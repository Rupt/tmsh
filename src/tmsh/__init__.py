# This file is adapted from Gmsh under the Gmsh License, which comprises the
# GNU General Public License with a custom exception, as stated below.
#
# This file has been changed from the Gmsh original as of 2025-04-21.
#
# Gmsh License
#
# Gmsh - Copyright (C) 1997-2024 C. Geuzaine, J.-F. Remacle
#
# Gmsh is provided under the terms of the GNU General Public License
# (GPL), Version 2 or later, with the following exception:
#
#   The copyright holders of Gmsh give you permission to combine Gmsh
#   with code included in the standard release of Netgen (from Joachim
#   Sch"oberl), METIS (from George Karypis at the University of
#   Minnesota), OpenCASCADE (from Open CASCADE S.A.S) and ParaView
#   (from Kitware, Inc.) under their respective licenses. You may copy
#   and distribute such a system following the terms of the GNU GPL for
#   Gmsh and the licenses of the other code concerned, provided that
#   you include the source code of that other code when and as the GNU
#   GPL requires distribution of source code.
#
#   Note that people who make modified versions of Gmsh are not
#   obligated to grant this special exception for their modified
#   versions; it is their choice whether to do so. The GNU General
#   Public License gives permission to release a modified version
#   without this exception; this exception also makes it possible to
#   release a modified version which carries forward this exception.
#
# End of exception.
#
# 		    GNU GENERAL PUBLIC LICENSE
# 		       Version 2, June 1991
#
#  Copyright (C) 1989, 1991 Free Software Foundation, Inc.
#  51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
#
# 			    Preamble
#
#   The licenses for most software are designed to take away your
# freedom to share and change it.  By contrast, the GNU General Public
# License is intended to guarantee your freedom to share and change free
# software--to make sure the software is free for all its users.  This
# General Public License applies to most of the Free Software
# Foundation's software and to any other program whose authors commit to
# using it.  (Some other Free Software Foundation software is covered by
# the GNU Library General Public License instead.)  You can apply it to
# your programs, too.
#
#   When we speak of free software, we are referring to freedom, not
# price.  Our General Public Licenses are designed to make sure that you
# have the freedom to distribute copies of free software (and charge for
# this service if you wish), that you receive source code or can get it
# if you want it, that you can change the software or use pieces of it
# in new free programs; and that you know you can do these things.
#
#   To protect your rights, we need to make restrictions that forbid
# anyone to deny you these rights or to ask you to surrender the rights.
# These restrictions translate to certain responsibilities for you if you
# distribute copies of the software, or if you modify it.
#
#   For example, if you distribute copies of such a program, whether
# gratis or for a fee, you must give the recipients all the rights that
# you have.  You must make sure that they, too, receive or can get the
# source code.  And you must show them these terms so they know their
# rights.
#
#   We protect your rights with two steps: (1) copyright the software, and
# (2) offer you this license which gives you legal permission to copy,
# distribute and/or modify the software.
#
#   Also, for each author's protection and ours, we want to make certain
# that everyone understands that there is no warranty for this free
# software.  If the software is modified by someone else and passed on, we
# want its recipients to know that what they have is not the original, so
# that any problems introduced by others will not reflect on the original
# authors' reputations.
#
#   Finally, any free program is threatened constantly by software
# patents.  We wish to avoid the danger that redistributors of a free
# program will individually obtain patent licenses, in effect making the
# program proprietary.  To prevent this, we have made it clear that any
# patent must be licensed for everyone's free use or not licensed at all.
#
#   The precise terms and conditions for copying, distribution and
# modification follow.
#
# 		    GNU GENERAL PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#   0. This License applies to any program or other work which contains
# a notice placed by the copyright holder saying it may be distributed
# under the terms of this General Public License.  The "Program", below,
# refers to any such program or work, and a "work based on the Program"
# means either the Program or any derivative work under copyright law:
# that is to say, a work containing the Program or a portion of it,
# either verbatim or with modifications and/or translated into another
# language.  (Hereinafter, translation is included without limitation in
# the term "modification".)  Each licensee is addressed as "you".
#
# Activities other than copying, distribution and modification are not
# covered by this License; they are outside its scope.  The act of
# running the Program is not restricted, and the output from the Program
# is covered only if its contents constitute a work based on the
# Program (independent of having been made by running the Program).
# Whether that is true depends on what the Program does.
#
#   1. You may copy and distribute verbatim copies of the Program's
# source code as you receive it, in any medium, provided that you
# conspicuously and appropriately publish on each copy an appropriate
# copyright notice and disclaimer of warranty; keep intact all the
# notices that refer to this License and to the absence of any warranty;
# and give any other recipients of the Program a copy of this License
# along with the Program.
#
# You may charge a fee for the physical act of transferring a copy, and
# you may at your option offer warranty protection in exchange for a fee.
#
#   2. You may modify your copy or copies of the Program or any portion
# of it, thus forming a work based on the Program, and copy and
# distribute such modifications or work under the terms of Section 1
# above, provided that you also meet all of these conditions:
#
#     a) You must cause the modified files to carry prominent notices
#     stating that you changed the files and the date of any change.
#
#     b) You must cause any work that you distribute or publish, that in
#     whole or in part contains or is derived from the Program or any
#     part thereof, to be licensed as a whole at no charge to all third
#     parties under the terms of this License.
#
#     c) If the modified program normally reads commands interactively
#     when run, you must cause it, when started running for such
#     interactive use in the most ordinary way, to print or display an
#     announcement including an appropriate copyright notice and a
#     notice that there is no warranty (or else, saying that you provide
#     a warranty) and that users may redistribute the program under
#     these conditions, and telling the user how to view a copy of this
#     License.  (Exception: if the Program itself is interactive but
#     does not normally print such an announcement, your work based on
#     the Program is not required to print an announcement.)
#
# These requirements apply to the modified work as a whole.  If
# identifiable sections of that work are not derived from the Program,
# and can be reasonably considered independent and separate works in
# themselves, then this License, and its terms, do not apply to those
# sections when you distribute them as separate works.  But when you
# distribute the same sections as part of a whole which is a work based
# on the Program, the distribution of the whole must be on the terms of
# this License, whose permissions for other licensees extend to the
# entire whole, and thus to each and every part regardless of who wrote it.
#
# Thus, it is not the intent of this section to claim rights or contest
# your rights to work written entirely by you; rather, the intent is to
# exercise the right to control the distribution of derivative or
# collective works based on the Program.
#
# In addition, mere aggregation of another work not based on the Program
# with the Program (or with a work based on the Program) on a volume of
# a storage or distribution medium does not bring the other work under
# the scope of this License.
#
#   3. You may copy and distribute the Program (or a work based on it,
# under Section 2) in object code or executable form under the terms of
# Sections 1 and 2 above provided that you also do one of the following:
#
#     a) Accompany it with the complete corresponding machine-readable
#     source code, which must be distributed under the terms of Sections
#     1 and 2 above on a medium customarily used for software interchange; or,
#
#     b) Accompany it with a written offer, valid for at least three
#     years, to give any third party, for a charge no more than your
#     cost of physically performing source distribution, a complete
#     machine-readable copy of the corresponding source code, to be
#     distributed under the terms of Sections 1 and 2 above on a medium
#     customarily used for software interchange; or,
#
#     c) Accompany it with the information you received as to the offer
#     to distribute corresponding source code.  (This alternative is
#     allowed only for noncommercial distribution and only if you
#     received the program in object code or executable form with such
#     an offer, in accord with Subsection b above.)
#
# The source code for a work means the preferred form of the work for
# making modifications to it.  For an executable work, complete source
# code means all the source code for all modules it contains, plus any
# associated interface definition files, plus the scripts used to
# control compilation and installation of the executable.  However, as a
# special exception, the source code distributed need not include
# anything that is normally distributed (in either source or binary
# form) with the major components (compiler, kernel, and so on) of the
# operating system on which the executable runs, unless that component
# itself accompanies the executable.
#
# If distribution of executable or object code is made by offering
# access to copy from a designated place, then offering equivalent
# access to copy the source code from the same place counts as
# distribution of the source code, even though third parties are not
# compelled to copy the source along with the object code.
#
#   4. You may not copy, modify, sublicense, or distribute the Program
# except as expressly provided under this License.  Any attempt
# otherwise to copy, modify, sublicense or distribute the Program is
# void, and will automatically terminate your rights under this License.
# However, parties who have received copies, or rights, from you under
# this License will not have their licenses terminated so long as such
# parties remain in full compliance.
#
#   5. You are not required to accept this License, since you have not
# signed it.  However, nothing else grants you permission to modify or
# distribute the Program or its derivative works.  These actions are
# prohibited by law if you do not accept this License.  Therefore, by
# modifying or distributing the Program (or any work based on the
# Program), you indicate your acceptance of this License to do so, and
# all its terms and conditions for copying, distributing or modifying
# the Program or works based on it.
#
#   6. Each time you redistribute the Program (or any work based on the
# Program), the recipient automatically receives a license from the
# original licensor to copy, distribute or modify the Program subject to
# these terms and conditions.  You may not impose any further
# restrictions on the recipients' exercise of the rights granted herein.
# You are not responsible for enforcing compliance by third parties to
# this License.
#
#   7. If, as a consequence of a court judgment or allegation of patent
# infringement or for any other reason (not limited to patent issues),
# conditions are imposed on you (whether by court order, agreement or
# otherwise) that contradict the conditions of this License, they do not
# excuse you from the conditions of this License.  If you cannot
# distribute so as to satisfy simultaneously your obligations under this
# License and any other pertinent obligations, then as a consequence you
# may not distribute the Program at all.  For example, if a patent
# license would not permit royalty-free redistribution of the Program by
# all those who receive copies directly or indirectly through you, then
# the only way you could satisfy both it and this License would be to
# refrain entirely from distribution of the Program.
#
# If any portion of this section is held invalid or unenforceable under
# any particular circumstance, the balance of the section is intended to
# apply and the section as a whole is intended to apply in other
# circumstances.
#
# It is not the purpose of this section to induce you to infringe any
# patents or other property right claims or to contest validity of any
# such claims; this section has the sole purpose of protecting the
# integrity of the free software distribution system, which is
# implemented by public license practices.  Many people have made
# generous contributions to the wide range of software distributed
# through that system in reliance on consistent application of that
# system; it is up to the author/donor to decide if he or she is willing
# to distribute software through any other system and a licensee cannot
# impose that choice.
#
# This section is intended to make thoroughly clear what is believed to
# be a consequence of the rest of this License.
#
#   8. If the distribution and/or use of the Program is restricted in
# certain countries either by patents or by copyrighted interfaces, the
# original copyright holder who places the Program under this License
# may add an explicit geographical distribution limitation excluding
# those countries, so that distribution is permitted only in or among
# countries not thus excluded.  In such case, this License incorporates
# the limitation as if written in the body of this License.
#
#   9. The Free Software Foundation may publish revised and/or new versions
# of the General Public License from time to time.  Such new versions will
# be similar in spirit to the present version, but may differ in detail to
# address new problems or concerns.
#
# Each version is given a distinguishing version number.  If the Program
# specifies a version number of this License which applies to it and "any
# later version", you have the option of following the terms and conditions
# either of that version or of any later version published by the Free
# Software Foundation.  If the Program does not specify a version number of
# this License, you may choose any version ever published by the Free Software
# Foundation.
#
#   10. If you wish to incorporate parts of the Program into other free
# programs whose distribution conditions are different, write to the author
# to ask for permission.  For software which is copyrighted by the Free
# Software Foundation, write to the Free Software Foundation; we sometimes
# make exceptions for this.  Our decision will be guided by the two goals
# of preserving the free status of all derivatives of our free software and
# of promoting the sharing and reuse of software generally.
#
# 			    NO WARRANTY
#
#   11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
# FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
# OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
# PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
# OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
# TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
# PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
# REPAIR OR CORRECTION.
#
#   12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
# WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
# REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
# INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
# OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
# TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
# YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
# PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGES.
#
# 		     END OF TERMS AND CONDITIONS
#
# End of Gmsh license

"""Type-annotated and linted Python interface for Gmsh."""

from __future__ import annotations

import ctypes
import math
import signal
from typing import TYPE_CHECKING, Literal

import gmsh

if TYPE_CHECKING:
    import builtins
    from collections.abc import Callable, Sequence
    from ctypes import (
        Array,
        _Pointer,
        c_char,
        c_char_p,
        c_double,
        c_int,
        c_size_t,
    )


def initialize(
    argv: Sequence[str] = (),
    *,
    readConfigFiles: bool = True,
    run: bool = False,
    interruptible: bool = True,
) -> None:
    """Initialize the Gmsh API.

    This must be called before any call to the other functions in the API. If
    `argv` is provided, it will be handled in the same way as the command line
    arguments in the Gmsh app. If `readConfigFiles` is set, read system Gmsh
    configuration files (gmshrc and gmsh-options). If `run` is set, run in the
    same way as the Gmsh app, either interactively or in batch mode depending
    on the command line arguments. If `run` is not set, initializing the API
    sets the options "General.AbortOnError" to 2 and "General.Terminal" to 1.
    """
    c_argc, c_argv = _iargcargv(argv)
    with _ErrorCode() as ierr:
        gmsh.lib.gmshInitialize(
            c_argc,
            c_argv,
            ctypes.c_int(bool(readConfigFiles)),
            ctypes.c_int(bool(run)),
            ctypes.byref(ierr),
        )
        if interruptible:
            gmsh.prev_interrupt_handler = signal.signal(
                signal.SIGINT, signal.SIG_DFL
            )


def isInitialized() -> int:
    """Return 1 if the Gmsh API is initialized, and 0 if not."""
    with _ErrorCode() as ierr:
        return gmsh.lib.gmshIsInitialized(ctypes.byref(ierr))


def finalize() -> None:
    """Finalize the Gmsh API.

    This must be called when you are done using the Gmsh API.
    """
    with _ErrorCode() as ierr:
        gmsh.lib.gmshFinalize(ctypes.byref(ierr))
        if gmsh.prev_interrupt_handler is not None:
            signal.signal(signal.SIGINT, gmsh.prev_interrupt_handler)


def open(fileName: str) -> None:  # noqa: A001
    """Open a file.

    Equivalent to the `File->Open' menu in the Gmsh app. Handling of the file
    depends on its extension and/or its contents: opening a file with model
    data will create a new model.
    """
    with _ErrorCode() as ierr:
        gmsh.lib.gmshOpen(
            ctypes.c_char_p(fileName.encode()), ctypes.byref(ierr)
        )


def merge(fileName: str) -> None:
    """Merge a file.

    Equivalent to the `File->Merge' menu in the Gmsh app.

    Handling of the file depends on its extension and/or its contents. Merging
    a file with model data will add the data to the current model.
    """
    with _ErrorCode() as ierr:
        gmsh.lib.gmshMerge(
            ctypes.c_char_p(fileName.encode()), ctypes.byref(ierr)
        )


def write(fileName: str) -> None:
    """Write a file.

    The export format is determined by the file extension.
    """
    with _ErrorCode() as ierr:
        gmsh.lib.gmshWrite(
            ctypes.c_char_p(fileName.encode()), ctypes.byref(ierr)
        )


def clear() -> None:
    """Clear Gmsh state.

    Clear all loaded models and post-processing data, and add a new empty model.
    """
    with _ErrorCode() as ierr:
        gmsh.lib.gmshClear(ctypes.byref(ierr))


class option:
    """Option handling functions."""

    @staticmethod
    def setNumber(name: str, value: float) -> None:
        """Set a numerical option to `value`.

        `name` is of the form "Category.Option" or "Category[num].Option".
        Available categories and options are listed in the "Gmsh options"
        chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-options).
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionSetNumber(
                ctypes.c_char_p(name.encode()),
                ctypes.c_double(value),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getNumber(name: str) -> float:
        """Return the `value` of a numerical option.

        `name` is of the form "Category.Option" or "Category[num].Option".
        Available categories and options are listed in the "Gmsh options"
        chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-options).
        """
        c_value = ctypes.c_double()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionGetNumber(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_value),
                ctypes.byref(ierr),
            )
        return c_value.value

    @staticmethod
    def setString(name: str, value: str) -> None:
        """Set a string option to `value`.

        `name` is of the form "Category.Option" or "Category[num].Option".
        Available categories and options are listed in the "Gmsh options"
        chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-options).
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionSetString(
                ctypes.c_char_p(name.encode()),
                ctypes.c_char_p(value.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getString(name: str) -> str:
        """Return the `value` of a string option.

        `name` is of the form "Category.Option" or "Category[num].Option".
        Available categories and options are listed in the "Gmsh options"
        chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-options).
        """
        c_value = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionGetString(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_value),
                ctypes.byref(ierr),
            )
        return _ostring(c_value)

    @staticmethod
    def setColor(name: str, r: int, g: int, b: int, a: int = 255) -> None:
        """Set a color option to the RGBA value (`r`, `g`, `b`, `a`).

        `r`, `g`, `b` and `a` should be integers between 0 and 255. `name` is
        of the form "Category.Color.Option" or "Category[num].Color.Option".
        Available categories and options are listed in the "Gmsh options"
        chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-options).
        For conciseness, "Color." can be omitted in `name`.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionSetColor(
                ctypes.c_char_p(name.encode()),
                ctypes.c_int(r),
                ctypes.c_int(g),
                ctypes.c_int(b),
                ctypes.c_int(a),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getColor(name: str) -> tuple[int, int, int, int]:
        """Return the `r`, `g`, `b`, `a` value of a color option.

        `name` is of the form "Category.Color.Option" or
        "Category[num].Color.Option". Available categories and options are
        listed in the "Gmsh options" chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-options).
        For conciseness "Color." can be omitted in `name`.
        """
        c_r = ctypes.c_int()
        c_g = ctypes.c_int()
        c_b = ctypes.c_int()
        c_a = ctypes.c_int()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionGetColor(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_r),
                ctypes.byref(c_g),
                ctypes.byref(c_b),
                ctypes.byref(c_a),
                ctypes.byref(ierr),
            )
        return (c_r.value, c_g.value, c_b.value, c_a.value)

    @staticmethod
    def restoreDefaults() -> None:
        """Restore all options to default settings."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOptionRestoreDefaults(ctypes.byref(ierr))


class model:
    """Model functions"""

    @staticmethod
    def add(name: str) -> None:
        """Add a new model with name `name` and set it as the current model."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelAdd(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def remove() -> None:
        """Remove the current model."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelRemove(ctypes.byref(ierr))

    @staticmethod
    def list() -> builtins.list[str]:
        """Return a list of the names of all models."""
        c_names, c_names_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelList(
                ctypes.byref(c_names),
                ctypes.byref(c_names_n),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_names, c_names_n.value)

    @staticmethod
    def getCurrent() -> str:
        """Return the name of the current model."""
        c_name = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetCurrent(
                ctypes.byref(c_name), ctypes.byref(ierr)
            )
        return _ostring(c_name)

    @staticmethod
    def setCurrent(name: str) -> None:
        """Set the current model to the model with name `name`.

        If several models have the same name, select the one that was added
        first.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetCurrent(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def getFileName() -> str:
        """Return the file name (if any) associated with the current model.

        A file name is associated when a model is read from a file on disk.
        """
        c_fileName = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetFileName(
                ctypes.byref(c_fileName), ctypes.byref(ierr)
            )
        return _ostring(c_fileName)

    @staticmethod
    def setFileName(fileName: str) -> None:
        """Set the file name associated with the current model."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetFileName(
                ctypes.c_char_p(fileName.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def getEntities(dim: int = -1) -> builtins.list[tuple[int, int]]:
        """Return the (dim, tag) pairs of all entities in the current model.

        A model entity is represented by two integers: its dimension (dim == 0,
        1, 2 or 3) and its tag (its unique, strictly positive identifier). If
        'dim' is >= 0, return only the entities of the specified dimension
        (e.g. points if 'dim' == 0). The entities are returned as a collection
        of (dim, tag) pairs.
        """
        c_dimTags = ctypes.POINTER(ctypes.c_int)()
        c_dimTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetEntities(
                ctypes.byref(c_dimTags),
                ctypes.byref(c_dimTags_n),
                ctypes.c_int(dim),
                ctypes.byref(ierr),
            )
        return _ovectorpair(c_dimTags, c_dimTags_n.value)

    @staticmethod
    def setEntityName(dim: int, tag: int, name: str) -> None:
        """Set the name of the entity of dimension 'dim' and tag 'tag'."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetEntityName(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.c_char_p(name.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getEntityName(dim: int, tag: int) -> str:
        """Return the name of the entity of dimension `dim` and tag `tag`."""
        c_name = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetEntityName(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_name),
                ctypes.byref(ierr),
            )
        return _ostring(c_name)

    @staticmethod
    def removeEntityName(name: str) -> None:
        """Replace the entity name `name` with `''` in the current model."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelRemoveEntityName(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def getPhysicalGroups(dim: int = -1) -> builtins.list[tuple[int, int]]:
        """Return all the physical groups in the current model.

        If `dim` is >= 0, return only the entities of the specified dimension
        (e.g. physical points if `dim` == 0). The entities are returned as a
        list of (dim, tag) pairs.
        """
        c_dimTags = ctypes.POINTER(ctypes.c_int)()
        c_dimTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetPhysicalGroups(
                ctypes.byref(c_dimTags),
                ctypes.byref(c_dimTags_n),
                ctypes.c_int(dim),
                ctypes.byref(ierr),
            )
        return _ovectorpair(c_dimTags, c_dimTags_n.value)

    @staticmethod
    def getEntitiesForPhysicalGroup(dim: int, tag: int) -> builtins.list[int]:
        """Return tags of entities in the matching physical group.

        This function selects the tags of the model entities making up the
        physical group of dimension `dim` and tag `tag`.
        """
        c_tags = ctypes.POINTER(ctypes.c_int)()
        c_tags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetEntitiesForPhysicalGroup(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_tags),
                ctypes.byref(c_tags_n),
                ctypes.byref(ierr),
            )
        return _ovectorint(c_tags, c_tags_n.value)

    @staticmethod
    def getEntitiesForPhysicalName(
        name: str,
    ) -> builtins.list[tuple[int, int]]:
        """Return all (dim, tag)s for entities in the named physical group."""
        c_dimTags = ctypes.POINTER(ctypes.c_int)()
        c_dimTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetEntitiesForPhysicalName(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_dimTags),
                ctypes.byref(c_dimTags_n),
                ctypes.byref(ierr),
            )
        return _ovectorpair(c_dimTags, c_dimTags_n.value)

    @staticmethod
    def getPhysicalGroupsForEntity(dim: int, tag: int) -> builtins.list[int]:
        """Return the tags of physical groups containing entity (dim, tag)."""
        c_physicalTags = ctypes.POINTER(ctypes.c_int)()
        c_physicalTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetPhysicalGroupsForEntity(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_physicalTags),
                ctypes.byref(c_physicalTags_n),
                ctypes.byref(ierr),
            )
        return _ovectorint(c_physicalTags, c_physicalTags_n.value)

    @staticmethod
    def addPhysicalGroup(
        dim: int, tags: Sequence[int], *, tag: int = -1, name: str = ""
    ) -> int:
        """Return the tag of a new physical group comprising tags of this dim.

        Add a physical group of dimension `dim`, grouping the model entities
        with tags `tags`. Return the tag of the physical group, equal to `tag`
        if `tag` is positive, or a new tag if `tag` < 0. Set the name of the
        physical group if `name` is not empty.
        """
        c_tags, c_tags_n = _ivectorint(tags)
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshModelAddPhysicalGroup(
                ctypes.c_int(dim),
                c_tags,
                c_tags_n,
                ctypes.c_int(tag),
                ctypes.c_char_p(name.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def removePhysicalGroups(dimTags: Sequence[tuple[int, int]] = ()) -> None:
        """Remove all physical groups, or only those identified in `dimTags`.

        If `dimTags` is empty, remove all groups. Otherwise, remove the
        physical groups `dimTags` (given as a sequence of (dim, tag) pairs)
        from the current model.
        """
        c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelRemovePhysicalGroups(
                c_dimTags, c_dimTags_n, ctypes.byref(ierr)
            )

    @staticmethod
    def setPhysicalName(dim: int, tag: int, name: str) -> None:
        """Set the name of the physical group with the given (dim, tag)."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetPhysicalName(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.c_char_p(name.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getPhysicalName(dim: int, tag: int) -> str:
        """Return the name of the physical group with the given (dim, tag)."""
        c_name = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetPhysicalName(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_name),
                ctypes.byref(ierr),
            )
        return _ostring(c_name)

    @staticmethod
    def removePhysicalName(name: str) -> None:
        """Replace the physical name `name` with `''` in the current model."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelRemovePhysicalName(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def setTag(dim: int, tag: int, newTag: int) -> None:
        """Move the tag of the entity identified by (dim, tag) to `newTag`."""
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetTag(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.c_int(newTag),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getBoundary(
        dimTags: Sequence[tuple[int, int]],
        *,
        combined: bool = True,
        oriented: bool = True,
        recursive: bool = False,
    ) -> builtins.list[tuple[int, int]]:
        """Return the (dim, tag) pairs of entities bounding the given entities.

        Extract the boundary of the model entities `dimTags`, given as a vector
        of (dim, tag) pairs.

        Return the boundary of the individual entities (if `combined` is false)
        or the boundary of the combined geometrical shape formed by all input
        entities (if `combined` is true).

        Return tags multiplied by the sign of the boundary entity if `oriented`
        is true.

        Apply the boundary operator recursively down to dimension 0 (i.e. to
        points) if `recursive` is true.
        """
        c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
        c_outDimTags = ctypes.POINTER(ctypes.c_int)()
        c_outDimTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetBoundary(
                c_dimTags,
                c_dimTags_n,
                ctypes.byref(c_outDimTags),
                ctypes.byref(c_outDimTags_n),
                ctypes.c_int(bool(combined)),
                ctypes.c_int(bool(oriented)),
                ctypes.c_int(bool(recursive)),
                ctypes.byref(ierr),
            )
        return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

    @staticmethod
    def getAdjacencies(
        dim: int, tag: int
    ) -> tuple[builtins.list[int], builtins.list[int]]:
        """Return the 'upward' and 'downward' adjacencies to entity (dim, tag).

        Returns:
            tuple (upward, downward), containing the tags of selected entities.
            The `upward` vector returns the tags of adjacent entities of
            dimension `dim` + 1; the `downward` vector returns the tags of
            adjacent entities of dimension `dim` - 1.
        """
        c_upward = ctypes.POINTER(ctypes.c_int)()
        c_upward_n = ctypes.c_size_t()
        c_downward = ctypes.POINTER(ctypes.c_int)()
        c_downward_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetAdjacencies(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_upward),
                ctypes.byref(c_upward_n),
                ctypes.byref(c_downward),
                ctypes.byref(c_downward_n),
                ctypes.byref(ierr),
            )
        return (
            _ovectorint(c_upward, c_upward_n.value),
            _ovectorint(c_downward, c_downward_n.value),
        )

    @staticmethod
    def getEntitiesInBoundingBox(
        xmin: float,
        ymin: float,
        zmin: float,
        xmax: float,
        ymax: float,
        zmax: float,
        *,
        dim: int = -1,
    ) -> builtins.list[tuple[int, int]]:
        """gmsh.model.getEntitiesInBoundingBox(xmin, ymin, zmin, xmax, ymax, zmax, dim=-1)

        Get the model entities in the bounding box defined by the two points
        (`xmin`, `ymin`, `zmin`) and (`xmax`, `ymax`, `zmax`). If `dim` is >= 0,
        return only the entities of the specified dimension (e.g. points if `dim`
        == 0).

        Return `dimTags`.

        Types:
        - `xmin`: double
        - `ymin`: double
        - `zmin`: double
        - `xmax`: double
        - `ymax`: double
        - `zmax`: double
        - `dimTags`: vector of pairs of integers
        - `dim`: integer
        """
        c_dimTags = ctypes.POINTER(ctypes.c_int)()
        c_dimTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetEntitiesInBoundingBox(
                ctypes.c_double(xmin),
                ctypes.c_double(ymin),
                ctypes.c_double(zmin),
                ctypes.c_double(xmax),
                ctypes.c_double(ymax),
                ctypes.c_double(zmax),
                ctypes.byref(c_dimTags),
                ctypes.byref(c_dimTags_n),
                ctypes.c_int(dim),
                ctypes.byref(ierr),
            )
        return _ovectorpair(c_dimTags, c_dimTags_n.value)

    @staticmethod
    def getBoundingBox(
        dim: int, tag: int
    ) -> tuple[float, float, float, float, float, float]:
        """gmsh.model.getBoundingBox(dim, tag)

        Get the bounding box (`xmin`, `ymin`, `zmin`), (`xmax`, `ymax`, `zmax`) of
        the model entity of dimension `dim` and tag `tag`. If `dim` and `tag` are
        negative, get the bounding box of the whole model.

        Return `xmin`, `ymin`, `zmin`, `xmax`, `ymax`, `zmax`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `xmin`: double
        - `ymin`: double
        - `zmin`: double
        - `xmax`: double
        - `ymax`: double
        - `zmax`: double
        """
        c_xmin = ctypes.c_double()
        c_ymin = ctypes.c_double()
        c_zmin = ctypes.c_double()
        c_xmax = ctypes.c_double()
        c_ymax = ctypes.c_double()
        c_zmax = ctypes.c_double()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetBoundingBox(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_xmin),
                ctypes.byref(c_ymin),
                ctypes.byref(c_zmin),
                ctypes.byref(c_xmax),
                ctypes.byref(c_ymax),
                ctypes.byref(c_zmax),
                ctypes.byref(ierr),
            )
        return (
            c_xmin.value,
            c_ymin.value,
            c_zmin.value,
            c_xmax.value,
            c_ymax.value,
            c_zmax.value,
        )

    @staticmethod
    def getDimension() -> int:
        """Return the geometrical dimension of the current model."""
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshModelGetDimension(ctypes.byref(ierr))

    @staticmethod
    def addDiscreteEntity(
        dim: int, tag: int = -1, boundary: Sequence[int] = ()
    ) -> int:
        """gmsh.model.addDiscreteEntity(dim, tag=-1, boundary=[])

        Add a discrete model entity (defined by a mesh) of dimension `dim` in the
        current model. Return the tag of the new discrete entity, equal to `tag` if
        `tag` is positive, or a new tag if `tag` < 0. `boundary` specifies the tags
        of the entities on the boundary of the discrete entity, if any. Specifying
        `boundary` allows Gmsh to construct the topology of the overall model.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `boundary`: vector of integers
        """
        c_boundary, c_boundary_n = _ivectorint(boundary)
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshModelAddDiscreteEntity(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_boundary,
                c_boundary_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def removeEntities(
        dimTags: Sequence[tuple[int, int]], *, recursive: bool = False
    ) -> None:
        """gmsh.model.removeEntities(dimTags, recursive=False)

        Remove the entities `dimTags` (given as a vector of (dim, tag) pairs) of
        the current model, provided that they are not on the boundary of (or
        embedded in) higher-dimensional entities. If `recursive` is true, remove
        all the entities on their boundaries, down to dimension 0.

        Types:
        - `dimTags`: vector of pairs of integers
        - `recursive`: boolean
        """
        c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelRemoveEntities(
                c_dimTags,
                c_dimTags_n,
                ctypes.c_int(bool(recursive)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getType(dim: int, tag: int) -> str:
        """Return the type of the entity identified by (dim, tag)."""
        c_entityType = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetType(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_entityType),
                ctypes.byref(ierr),
            )
        return _ostring(c_entityType)

    @staticmethod
    def getParent(dim: int, tag: int) -> tuple[int, int]:
        """gmsh.model.getParent(dim, tag)

        In a partitioned model, get the parent of the entity of dimension `dim` and
        tag `tag`, i.e. from which the entity is a part of, if any. `parentDim` and
        `parentTag` are set to -1 if the entity has no parent.

        Return `parentDim`, `parentTag`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `parentDim`: integer
        - `parentTag`: integer
        """
        c_parentDim = ctypes.c_int()
        c_parentTag = ctypes.c_int()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetParent(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_parentDim),
                ctypes.byref(c_parentTag),
                ctypes.byref(ierr),
            )
        return c_parentDim.value, c_parentTag.value

    @staticmethod
    def getNumberOfPartitions() -> int:
        """Return the number of partitions in the model."""
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshModelGetNumberOfPartitions(ctypes.byref(ierr))

    @staticmethod
    def getPartitions(dim: int, tag: int) -> builtins.list[int]:
        """gmsh.model.getPartitions(dim, tag)

        In a partitioned model, return the tags of the partition(s) to which the
        entity belongs.

        Return `partitions`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `partitions`: vector of integers
        """
        c_partitions = ctypes.POINTER(ctypes.c_int)()
        c_partitions_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetPartitions(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_partitions),
                ctypes.byref(c_partitions_n),
                ctypes.byref(ierr),
            )
        return _ovectorint(c_partitions, c_partitions_n.value)

    @staticmethod
    def getValue(
        dim: int, tag: int, parametricCoord: Sequence[float]
    ) -> builtins.list[float]:
        """gmsh.model.getValue(dim, tag, parametricCoord)

        Evaluate the parametrization of the entity of dimension `dim` and tag `tag`
        at the parametric coordinates `parametricCoord`. Only valid for `dim` equal
        to 0 (with empty `parametricCoord`), 1 (with `parametricCoord` containing
        parametric coordinates on the curve) or 2 (with `parametricCoord`
        containing u, v parametric coordinates on the surface, concatenated: [p1u,
        p1v, p2u, ...]). Return x, y, z coordinates in `coord`, concatenated: [p1x,
        p1y, p1z, p2x, ...].

        Return `coord`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `coord`: vector of doubles
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_coord = ctypes.POINTER(ctypes.c_double)()
        c_coord_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetValue(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.byref(c_coord),
                ctypes.byref(c_coord_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_coord, c_coord_n.value)

    @staticmethod
    def getDerivative(
        dim: int, tag: int, parametricCoord: Sequence[float]
    ) -> builtins.list[float]:
        """gmsh.model.getDerivative(dim, tag, parametricCoord)

        Evaluate the derivative of the parametrization of the entity of dimension
        `dim` and tag `tag` at the parametric coordinates `parametricCoord`. Only
        valid for `dim` equal to 1 (with `parametricCoord` containing parametric
        coordinates on the curve) or 2 (with `parametricCoord` containing u, v
        parametric coordinates on the surface, concatenated: [p1u, p1v, p2u, ...]).
        For `dim` equal to 1 return the x, y, z components of the derivative with
        respect to u [d1ux, d1uy, d1uz, d2ux, ...]; for `dim` equal to 2 return the
        x, y, z components of the derivative with respect to u and v: [d1ux, d1uy,
        d1uz, d1vx, d1vy, d1vz, d2ux, ...].

        Return `derivatives`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `derivatives`: vector of doubles
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_derivatives = ctypes.POINTER(ctypes.c_double)()
        c_derivatives_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetDerivative(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.byref(c_derivatives),
                ctypes.byref(c_derivatives_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_derivatives, c_derivatives_n.value)

    @staticmethod
    def getSecondDerivative(
        dim: int, tag: int, parametricCoord: Sequence[float]
    ) -> builtins.list[float]:
        """gmsh.model.getSecondDerivative(dim, tag, parametricCoord)

        Evaluate the second derivative of the parametrization of the entity of
        dimension `dim` and tag `tag` at the parametric coordinates
        `parametricCoord`. Only valid for `dim` equal to 1 (with `parametricCoord`
        containing parametric coordinates on the curve) or 2 (with
        `parametricCoord` containing u, v parametric coordinates on the surface,
        concatenated: [p1u, p1v, p2u, ...]). For `dim` equal to 1 return the x, y,
        z components of the second derivative with respect to u [d1uux, d1uuy,
        d1uuz, d2uux, ...]; for `dim` equal to 2 return the x, y, z components of
        the second derivative with respect to u and v, and the mixed derivative
        with respect to u and v: [d1uux, d1uuy, d1uuz, d1vvx, d1vvy, d1vvz, d1uvx,
        d1uvy, d1uvz, d2uux, ...].

        Return `derivatives`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `derivatives`: vector of doubles
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_derivatives = ctypes.POINTER(ctypes.c_double)()
        c_derivatives_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetSecondDerivative(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.byref(c_derivatives),
                ctypes.byref(c_derivatives_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_derivatives, c_derivatives_n.value)

    @staticmethod
    def getCurvature(
        dim: int, tag: int, parametricCoord: Sequence[float]
    ) -> builtins.list[float]:
        """gmsh.model.getCurvature(dim, tag, parametricCoord)

        Evaluate the (maximum) curvature of the entity of dimension `dim` and tag
        `tag` at the parametric coordinates `parametricCoord`. Only valid for `dim`
        equal to 1 (with `parametricCoord` containing parametric coordinates on the
        curve) or 2 (with `parametricCoord` containing u, v parametric coordinates
        on the surface, concatenated: [p1u, p1v, p2u, ...]).

        Return `curvatures`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `curvatures`: vector of doubles
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_curvatures = ctypes.POINTER(ctypes.c_double)()
        c_curvatures_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetCurvature(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.byref(c_curvatures),
                ctypes.byref(c_curvatures_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_curvatures, c_curvatures_n.value)

    @staticmethod
    def getPrincipalCurvatures(
        tag: int, parametricCoord: Sequence[float]
    ) -> tuple[
        builtins.list[float],
        builtins.list[float],
        builtins.list[float],
        builtins.list[float],
    ]:
        """gmsh.model.getPrincipalCurvatures(tag, parametricCoord)

        Evaluate the principal curvatures of the surface with tag `tag` at the
        parametric coordinates `parametricCoord`, as well as their respective
        directions. `parametricCoord` are given by pair of u and v coordinates,
        concatenated: [p1u, p1v, p2u, ...].

        Return `curvatureMax`, `curvatureMin`, `directionMax`, `directionMin`.

        Types:
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `curvatureMax`: vector of doubles
        - `curvatureMin`: vector of doubles
        - `directionMax`: vector of doubles
        - `directionMin`: vector of doubles
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_curvatureMax = ctypes.POINTER(ctypes.c_double)()
        c_curvatureMax_n = ctypes.c_size_t()
        c_curvatureMin = ctypes.POINTER(ctypes.c_double)()
        c_curvatureMin_n = ctypes.c_size_t()
        c_directionMax = ctypes.POINTER(ctypes.c_double)()
        c_directionMax_n = ctypes.c_size_t()
        c_directionMin = ctypes.POINTER(ctypes.c_double)()
        c_directionMin_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetPrincipalCurvatures(
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.byref(c_curvatureMax),
                ctypes.byref(c_curvatureMax_n),
                ctypes.byref(c_curvatureMin),
                ctypes.byref(c_curvatureMin_n),
                ctypes.byref(c_directionMax),
                ctypes.byref(c_directionMax_n),
                ctypes.byref(c_directionMin),
                ctypes.byref(c_directionMin_n),
                ctypes.byref(ierr),
            )
        return (
            _ovectordouble(c_curvatureMax, c_curvatureMax_n.value),
            _ovectordouble(c_curvatureMin, c_curvatureMin_n.value),
            _ovectordouble(c_directionMax, c_directionMax_n.value),
            _ovectordouble(c_directionMin, c_directionMin_n.value),
        )

    @staticmethod
    def getNormal(
        tag: int, parametricCoord: Sequence[float]
    ) -> builtins.list[float]:
        """gmsh.model.getNormal(tag, parametricCoord)

        Get the normal to the surface with tag `tag` at the parametric coordinates
        `parametricCoord`. The `parametricCoord` vector should contain u and v
        coordinates, concatenated: [p1u, p1v, p2u, ...]. `normals` are returned as
        a vector of x, y, z components, concatenated: [n1x, n1y, n1z, n2x, ...].

        Return `normals`.

        Types:
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `normals`: vector of doubles
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_normals = ctypes.POINTER(ctypes.c_double)()
        c_normals_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetNormal(
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.byref(c_normals),
                ctypes.byref(c_normals_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_normals, c_normals_n.value)

    @staticmethod
    def getParametrization(
        dim: int, tag: int, coord: Sequence[float]
    ) -> builtins.list[float]:
        """gmsh.model.getParametrization(dim, tag, coord)

        Get the parametric coordinates `parametricCoord` for the points `coord` on
        the entity of dimension `dim` and tag `tag`. `coord` are given as x, y, z
        coordinates, concatenated: [p1x, p1y, p1z, p2x, ...]. `parametricCoord`
        returns the parametric coordinates t on the curve (if `dim` = 1) or u and v
        coordinates concatenated on the surface (if `dim` == 2), i.e. [p1t, p2t,
        ...] or [p1u, p1v, p2u, ...].

        Return `parametricCoord`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `coord`: vector of doubles
        - `parametricCoord`: vector of doubles
        """
        c_coord, c_coord_n = _ivectordouble(coord)
        c_parametricCoord = ctypes.POINTER(ctypes.c_double)()
        c_parametricCoord_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetParametrization(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_coord,
                c_coord_n,
                ctypes.byref(c_parametricCoord),
                ctypes.byref(c_parametricCoord_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_parametricCoord, c_parametricCoord_n.value)

    @staticmethod
    def getParametrizationBounds(
        dim: int, tag: int
    ) -> tuple[builtins.list[float], builtins.list[float]]:
        """gmsh.model.getParametrizationBounds(dim, tag)

        Get the `min` and `max` bounds of the parametric coordinates for the entity
        of dimension `dim` and tag `tag`.

        Return `min`, `max`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `min`: vector of doubles
        - `max`: vector of doubles
        """
        c_min, c_min_n = (ctypes.POINTER(ctypes.c_double)(), ctypes.c_size_t())
        c_max, c_max_n = (ctypes.POINTER(ctypes.c_double)(), ctypes.c_size_t())
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetParametrizationBounds(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_min),
                ctypes.byref(c_min_n),
                ctypes.byref(c_max),
                ctypes.byref(c_max_n),
                ctypes.byref(ierr),
            )
        return (
            _ovectordouble(c_min, c_min_n.value),
            _ovectordouble(c_max, c_max_n.value),
        )

    @staticmethod
    def isInside(
        dim: int, tag: int, coord: Sequence[float], *, parametric: bool = False
    ) -> int:
        """gmsh.model.isInside(dim, tag, coord, parametric=False)

        Check if the coordinates (or the parametric coordinates if `parametric` is
        set) provided in `coord` correspond to points inside the entity of
        dimension `dim` and tag `tag`, and return the number of points inside. This
        feature is only available for a subset of entities, depending on the
        underlying geometrical representation.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `coord`: vector of doubles
        - `parametric`: boolean
        """
        c_coord, c_coord_n = _ivectordouble(coord)
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshModelIsInside(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_coord,
                c_coord_n,
                ctypes.c_int(bool(parametric)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getClosestPoint(
        dim: int, tag: int, coord: Sequence[float]
    ) -> tuple[builtins.list[float], builtins.list[float]]:
        """gmsh.model.getClosestPoint(dim, tag, coord)

        Get the points `closestCoord` on the entity of dimension `dim` and tag
        `tag` to the points `coord`, by orthogonal projection. `coord` and
        `closestCoord` are given as x, y, z coordinates, concatenated: [p1x, p1y,
        p1z, p2x, ...]. `parametricCoord` returns the parametric coordinates t on
        the curve (if `dim` == 1) or u and v coordinates concatenated on the
        surface (if `dim` = 2), i.e. [p1t, p2t, ...] or [p1u, p1v, p2u, ...].

        Return `closestCoord`, `parametricCoord`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `coord`: vector of doubles
        - `closestCoord`: vector of doubles
        - `parametricCoord`: vector of doubles
        """
        c_coord, c_coord_n = _ivectordouble(coord)
        c_closestCoord = ctypes.POINTER(ctypes.c_double)()
        c_closestCoord_n = ctypes.c_size_t()
        c_parametricCoord = ctypes.POINTER(ctypes.c_double)()
        c_parametricCoord_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetClosestPoint(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_coord,
                c_coord_n,
                ctypes.byref(c_closestCoord),
                ctypes.byref(c_closestCoord_n),
                ctypes.byref(c_parametricCoord),
                ctypes.byref(c_parametricCoord_n),
                ctypes.byref(ierr),
            )
        return (
            _ovectordouble(c_closestCoord, c_closestCoord_n.value),
            _ovectordouble(c_parametricCoord, c_parametricCoord_n.value),
        )

    @staticmethod
    def reparametrizeOnSurface(
        dim: int,
        tag: int,
        parametricCoord: Sequence[float],
        surfaceTag: int,
        *,
        which: int = 0,
    ) -> builtins.list[float]:
        """gmsh.model.reparametrizeOnSurface(dim, tag, parametricCoord, surfaceTag, which=0)

        Reparametrize the boundary entity (point or curve, i.e. with `dim` == 0 or
        `dim` == 1) of tag `tag` on the surface `surfaceTag`. If `dim` == 1,
        reparametrize all the points corresponding to the parametric coordinates
        `parametricCoord`. Multiple matches in case of periodic surfaces can be
        selected with `which`. This feature is only available for a subset of
        entities, depending on the underlying geometrical representation.

        Return `surfaceParametricCoord`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `parametricCoord`: vector of doubles
        - `surfaceTag`: integer
        - `surfaceParametricCoord`: vector of doubles
        - `which`: integer
        """
        c_parametricCoord, c_parametricCoord_n = _ivectordouble(
            parametricCoord
        )
        c_surfaceParametricCoord = ctypes.POINTER(ctypes.c_double)()
        c_surfaceParametricCoord_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelReparametrizeOnSurface(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                c_parametricCoord,
                c_parametricCoord_n,
                ctypes.c_int(surfaceTag),
                ctypes.byref(c_surfaceParametricCoord),
                ctypes.byref(c_surfaceParametricCoord_n),
                ctypes.c_int(which),
                ctypes.byref(ierr),
            )
        return _ovectordouble(
            c_surfaceParametricCoord, c_surfaceParametricCoord_n.value
        )

    @staticmethod
    def setVisibility(
        dimTags: Sequence[tuple[int, int]],
        value: int,
        *,
        recursive: bool = False,
    ) -> None:
        """gmsh.model.setVisibility(dimTags, value, recursive=False)

        Set the visibility of the model entities `dimTags` (given as a vector of
        (dim, tag) pairs) to `value`. Apply the visibility setting recursively if
        `recursive` is true.

        Types:
        - `dimTags`: vector of pairs of integers
        - `value`: integer
        - `recursive`: boolean
        """
        c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetVisibility(
                c_dimTags,
                c_dimTags_n,
                ctypes.c_int(value),
                ctypes.c_int(bool(recursive)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getVisibility(dim: int, tag: int) -> int:
        """gmsh.model.getVisibility(dim, tag)

        Get the visibility of the model entity of dimension `dim` and tag `tag`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `value`: integer
        """
        c_value = ctypes.c_int()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetVisibility(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_value),
                ctypes.byref(ierr),
            )
        return c_value.value

    @staticmethod
    def setVisibilityPerWindow(value: int, *, windowIndex: int = 0) -> None:
        """gmsh.model.setVisibilityPerWindow(value, windowIndex=0)

        Set the global visibility of the model per window to `value`, where
        `windowIndex` identifies the window in the window list.

        Types:
        - `value`: integer
        - `windowIndex`: integer
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetVisibilityPerWindow(
                ctypes.c_int(value),
                ctypes.c_int(windowIndex),
                ctypes.byref(ierr),
            )

    @staticmethod
    def setColor(
        dimTags: Sequence[tuple[int, int]],
        r: int,
        g: int,
        b: int,
        a: int = 255,
        *,
        recursive: bool = False,
    ) -> None:
        """gmsh.model.setColor(dimTags, r, g, b, a=255, recursive=False)

        Set the color of the model entities `dimTags` (given as a vector of (dim,
        tag) pairs) to the RGBA value (`r`, `g`, `b`, `a`), where `r`, `g`, `b` and
        `a` should be integers between 0 and 255. Apply the color setting
        recursively if `recursive` is true.

        Types:
        - `dimTags`: vector of pairs of integers
        - `r`: integer
        - `g`: integer
        - `b`: integer
        - `a`: integer
        - `recursive`: boolean
        """
        c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetColor(
                c_dimTags,
                c_dimTags_n,
                ctypes.c_int(r),
                ctypes.c_int(g),
                ctypes.c_int(b),
                ctypes.c_int(a),
                ctypes.c_int(bool(recursive)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getColor(dim: int, tag: int) -> tuple[int, int, int, int]:
        """gmsh.model.getColor(dim, tag)

        Get the color of the model entity of dimension `dim` and tag `tag`. If no
        color is specified for the entity, return fully transparent blue, i.e. (0,
        0, 255, 0).

        Return `r`, `g`, `b`, `a`.

        Types:
        - `dim`: integer
        - `tag`: integer
        - `r`: integer
        - `g`: integer
        - `b`: integer
        - `a`: integer
        """
        c_r = ctypes.c_int()
        c_g = ctypes.c_int()
        c_b = ctypes.c_int()
        c_a = ctypes.c_int()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetColor(
                ctypes.c_int(dim),
                ctypes.c_int(tag),
                ctypes.byref(c_r),
                ctypes.byref(c_g),
                ctypes.byref(c_b),
                ctypes.byref(c_a),
                ctypes.byref(ierr),
            )
        return (c_r.value, c_g.value, c_b.value, c_a.value)

    @staticmethod
    def setCoordinates(tag: int, x: float, y: float, z: float) -> None:
        """gmsh.model.setCoordinates(tag, x, y, z)

        Set the `x`, `y`, `z` coordinates of a geometrical point.

        Types:
        - `tag`: integer
        - `x`: double
        - `y`: double
        - `z`: double
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetCoordinates(
                ctypes.c_int(tag),
                ctypes.c_double(x),
                ctypes.c_double(y),
                ctypes.c_double(z),
                ctypes.byref(ierr),
            )

    @staticmethod
    def setAttribute(name: str, values: Sequence[str]) -> None:
        """gmsh.model.setAttribute(name, values)

        Set the values of the attribute with name `name`.

        Types:
        - `name`: string
        - `values`: vector of strings
        """
        c_values, c_values_n = _ivectorstring(values)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelSetAttribute(
                ctypes.c_char_p(name.encode()),
                c_values,
                c_values_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def getAttribute(name: str) -> builtins.list[str]:
        """gmsh.model.getAttribute(name)

        Get the values of the attribute with name `name`.

        Return `values`.

        Types:
        - `name`: string
        - `values`: vector of strings
        """
        c_values, c_values_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetAttribute(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_values),
                ctypes.byref(c_values_n),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_values, c_values_n.value)

    @staticmethod
    def getAttributeNames() -> builtins.list[str]:
        """gmsh.model.getAttributeNames()

        Get the names of any optional attributes stored in the model.

        Return `names`.

        Types:
        - `names`: vector of strings
        """
        c_names, c_names_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelGetAttributeNames(
                ctypes.byref(c_names),
                ctypes.byref(c_names_n),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_names, c_names_n.value)

    @staticmethod
    def removeAttribute(name: str) -> None:
        """gmsh.model.removeAttribute(name)

        Remove the attribute with name `name`.

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshModelRemoveAttribute(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    class mesh:
        """Mesh functions"""

        @staticmethod
        def generate(dim: Literal[0, 1, 2, 3] = 3) -> None:
            """gmsh.model.mesh.generate(dim=3)

            Generate a mesh of the current model, up to dimension `dim` (0, 1, 2 or 3).

            Types:
            - `dim`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGenerate(
                    ctypes.c_int(dim), ctypes.byref(ierr)
                )

        @staticmethod
        def partition(
            numPart: int,
            *,
            elementTags: Sequence[int] = (),
            partitions: Sequence[int] = (),
        ) -> None:
            """gmsh.model.mesh.partition(numPart, elementTags=[], partitions=[])

            Partition the mesh of the current model into `numPart` partitions.
            Optionally, `elementTags` and `partitions` can be provided to specify the
            partition of each element explicitly.

            Types:
            - `numPart`: integer
            - `elementTags`: vector of sizes
            - `partitions`: vector of integers
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            c_partitions, c_partitions_n = _ivectorint(partitions)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshPartition(
                    ctypes.c_int(numPart),
                    c_elementTags,
                    c_elementTags_n,
                    c_partitions,
                    c_partitions_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def unpartition() -> None:
            """gmsh.model.mesh.unpartition()

            Unpartition the mesh of the current model.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshUnpartition(ctypes.byref(ierr))

        @staticmethod
        def optimize(
            *,
            method: str = "",
            force: bool = False,
            niter: int = 1,
            dimTags: Sequence[tuple[int, int]] = (),
        ) -> None:
            """gmsh.model.mesh.optimize(method="", force=False, niter=1, dimTags=[])

            Optimize the mesh of the current model using `method` (empty for default
            tetrahedral mesh optimizer, "Netgen" for Netgen optimizer, "HighOrder" for
            direct high-order mesh optimizer, "HighOrderElastic" for high-order elastic
            smoother, "HighOrderFastCurving" for fast curving algorithm, "Laplace2D"
            for Laplace smoothing, "Relocate2D" and "Relocate3D" for node relocation,
            "QuadQuasiStructured" for quad mesh optimization, "UntangleMeshGeometry"
            for untangling). If `force` is set apply the optimization also to discrete
            entities. If `dimTags` (given as a vector of (dim, tag) pairs) is given,
            only apply the optimizer to the given entities.

            Types:
            - `method`: string
            - `force`: boolean
            - `niter`: integer
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshOptimize(
                    ctypes.c_char_p(method.encode()),
                    ctypes.c_int(bool(force)),
                    ctypes.c_int(niter),
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def recombine() -> None:
            """gmsh.model.mesh.recombine()

            Recombine the mesh of the current model.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRecombine(ctypes.byref(ierr))

        @staticmethod
        def refine() -> None:
            """gmsh.model.mesh.refine()

            Refine the mesh of the current model by uniformly splitting the elements.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRefine(ctypes.byref(ierr))

        @staticmethod
        def setOrder(order: int) -> None:
            """gmsh.model.mesh.setOrder(order)

            Change the order of the elements in the mesh of the current model to
            `order`.

            Types:
            - `order`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetOrder(
                    ctypes.c_int(order), ctypes.byref(ierr)
                )

        @staticmethod
        def getLastEntityError() -> list[tuple[int, int]]:
            """gmsh.model.mesh.getLastEntityError()

            Get the last entities `dimTags` (as a vector of (dim, tag) pairs) where a
            meshing error occurred. Currently only populated by the new 3D meshing
            algorithms.

            Return `dimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags = ctypes.POINTER(ctypes.c_int)()
            c_dimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetLastEntityError(
                    ctypes.byref(c_dimTags),
                    ctypes.byref(c_dimTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_dimTags, c_dimTags_n.value)

        @staticmethod
        def getLastNodeError() -> list[int]:
            """gmsh.model.mesh.getLastNodeError()

            Get the last node tags `nodeTags` where a meshing error occurred. Currently
            only populated by the new 3D meshing algorithms.

            Return `nodeTags`.

            Types:
            - `nodeTags`: vector of sizes
            """
            c_nodeTags = ctypes.POINTER(ctypes.c_size_t)()
            c_nodeTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetLastNodeError(
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_nodeTags, c_nodeTags_n.value)

        @staticmethod
        def clear(dimTags: Sequence[tuple[int, int]] = ()) -> None:
            """gmsh.model.mesh.clear(dimTags=[])

            Clear the mesh, i.e. delete all the nodes and elements, for the entities
            `dimTags`, given as a vector of (dim, tag) pairs. If `dimTags` is empty,
            clear the whole mesh. Note that the mesh of an entity can only be cleared
            if this entity is not on the boundary of another entity with a non-empty
            mesh.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshClear(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def removeElements(
            dim: int, tag: int, elementTags: Sequence[int] = ()
        ) -> None:
            """gmsh.model.mesh.removeElements(dim, tag, elementTags=[])

            Remove the elements with tags `elementTags` from the entity of dimension
            `dim` and tag `tag`. If `elementTags` is empty, remove all the elements
            classified on the entity. To get consistent node classification on model
            entities, `reclassifyNodes()' should be called afterwards.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `elementTags`: vector of sizes
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRemoveElements(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    c_elementTags,
                    c_elementTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def reverse(dimTags: Sequence[tuple[int, int]] = ()) -> None:
            """gmsh.model.mesh.reverse(dimTags=[])

            Reverse the orientation of the elements in the entities `dimTags`, given as
            a vector of (dim, tag) pairs. If `dimTags` is empty, reverse the
            orientation of the elements in the whole mesh.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshReverse(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def reverseElements(elementTags: Sequence[int]) -> None:
            """gmsh.model.mesh.reverseElements(elementTags)

            Reverse the orientation of the elements with tags `elementTags`.

            Types:
            - `elementTags`: vector of sizes
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshReverseElements(
                    c_elementTags, c_elementTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def affineTransform(
            affineTransform: Sequence[float],
            dimTags: Sequence[tuple[int, int]] = (),
        ) -> None:
            """gmsh.model.mesh.affineTransform(affineTransform, dimTags=[])

            Apply the affine transformation `affineTransform` (16 entries of a 4x4
            matrix, by row; only the 12 first can be provided for convenience) to the
            coordinates of the nodes classified on the entities `dimTags`, given as a
            vector of (dim, tag) pairs. If `dimTags` is empty, transform all the nodes
            in the mesh.

            Types:
            - `affineTransform`: vector of doubles
            - `dimTags`: vector of pairs of integers
            """
            c_affineTransform, c_affineTransform_n = _ivectordouble(
                affineTransform
            )
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAffineTransform(
                    c_affineTransform,
                    c_affineTransform_n,
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getNodes(
            dim: int = -1,
            tag: int = -1,
            *,
            includeBoundary: bool = False,
            returnParametricCoord: bool = True,
        ) -> tuple[list[int], list[float], list[float]]:
            """gmsh.model.mesh.getNodes(dim=-1, tag=-1, includeBoundary=False, returnParametricCoord=True)

            Get the nodes classified on the entity of dimension `dim` and tag `tag`. If
            `tag` < 0, get the nodes for all entities of dimension `dim`. If `dim` and
            `tag` are negative, get all the nodes in the mesh. `nodeTags` contains the
            node tags (their unique, strictly positive identification numbers). `coord`
            is a vector of length 3 times the length of `nodeTags` that contains the x,
            y, z coordinates of the nodes, concatenated: [n1x, n1y, n1z, n2x, ...]. If
            `dim` >= 0 and `returnParamtricCoord` is set, `parametricCoord` contains
            the parametric coordinates ([u1, u2, ...] or [u1, v1, u2, ...]) of the
            nodes, if available. The length of `parametricCoord` can be 0 or `dim`
            times the length of `nodeTags`. If `includeBoundary` is set, also return
            the nodes classified on the boundary of the entity (which will be
            reparametrized on the entity if `dim` >= 0 in order to compute their
            parametric coordinates).

            Return `nodeTags`, `coord`, `parametricCoord`.

            Types:
            - `nodeTags`: vector of sizes
            - `coord`: vector of doubles
            - `parametricCoord`: vector of doubles
            - `dim`: integer
            - `tag`: integer
            - `includeBoundary`: boolean
            - `returnParametricCoord`: boolean
            """
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            c_parametricCoord = ctypes.POINTER(ctypes.c_double)()
            c_parametricCoord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetNodes(
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.byref(c_parametricCoord),
                    ctypes.byref(c_parametricCoord_n),
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(includeBoundary)),
                    ctypes.c_int(bool(returnParametricCoord)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
                _ovectordouble(c_parametricCoord, c_parametricCoord_n.value),
            )

        @staticmethod
        def getNodesByElementType(
            elementType: int,
            *,
            tag: int = -1,
            returnParametricCoord: bool = True,
        ) -> tuple[list[int], list[float], list[float]]:
            """gmsh.model.mesh.getNodesByElementType(elementType, tag=-1, returnParametricCoord=True)

            Get the nodes classified on the entity of tag `tag`, for all the elements
            of type `elementType`. The other arguments are treated as in `getNodes`.

            Return `nodeTags`, `coord`, `parametricCoord`.

            Types:
            - `elementType`: integer
            - `nodeTags`: vector of sizes
            - `coord`: vector of doubles
            - `parametricCoord`: vector of doubles
            - `tag`: integer
            - `returnParametricCoord`: boolean
            """
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            c_parametricCoord = ctypes.POINTER(ctypes.c_double)()
            c_parametricCoord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetNodesByElementType(
                    ctypes.c_int(elementType),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.byref(c_parametricCoord),
                    ctypes.byref(c_parametricCoord_n),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(returnParametricCoord)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
                _ovectordouble(c_parametricCoord, c_parametricCoord_n.value),
            )

        @staticmethod
        def getNode(nodeTag: int) -> tuple[list[float], list[float], int, int]:
            """gmsh.model.mesh.getNode(nodeTag)

            Get the coordinates and the parametric coordinates (if any) of the node
            with tag `tag`, as well as the dimension `dim` and tag `tag` of the entity
            on which the node is classified. This function relies on an internal cache
            (a vector in case of dense node numbering, a map otherwise); for large
            meshes accessing nodes in bulk is often preferable.

            Return `coord`, `parametricCoord`, `dim`, `tag`.

            Types:
            - `nodeTag`: size
            - `coord`: vector of doubles
            - `parametricCoord`: vector of doubles
            - `dim`: integer
            - `tag`: integer
            """
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            c_parametricCoord = ctypes.POINTER(ctypes.c_double)()
            c_parametricCoord_n = ctypes.c_size_t()
            c_dim = ctypes.c_int()
            c_tag = ctypes.c_int()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetNode(
                    ctypes.c_size_t(nodeTag),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.byref(c_parametricCoord),
                    ctypes.byref(c_parametricCoord_n),
                    ctypes.byref(c_dim),
                    ctypes.byref(c_tag),
                    ctypes.byref(ierr),
                )

            return (
                _ovectordouble(c_coord, c_coord_n.value),
                _ovectordouble(c_parametricCoord, c_parametricCoord_n.value),
                c_dim.value,
                c_tag.value,
            )

        @staticmethod
        def setNode(
            nodeTag: int,
            coord: Sequence[float],
            parametricCoord: Sequence[float],
        ) -> None:
            """gmsh.model.mesh.setNode(nodeTag, coord, parametricCoord)

            Set the coordinates and the parametric coordinates (if any) of the node
            with tag `tag`. This function relies on an internal cache (a vector in case
            of dense node numbering, a map otherwise); for large meshes accessing nodes
            in bulk is often preferable.

            Types:
            - `nodeTag`: size
            - `coord`: vector of doubles
            - `parametricCoord`: vector of doubles
            """
            c_coord, c_coord_n = _ivectordouble(coord)
            c_parametricCoord, c_parametricCoord_n = _ivectordouble(
                parametricCoord
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetNode(
                    ctypes.c_size_t(nodeTag),
                    c_coord,
                    c_coord_n,
                    c_parametricCoord,
                    c_parametricCoord_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def rebuildNodeCache(*, onlyIfNecessary: bool = True) -> None:
            """gmsh.model.mesh.rebuildNodeCache(onlyIfNecessary=True)

            Rebuild the node cache.

            Types:
            - `onlyIfNecessary`: boolean
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRebuildNodeCache(
                    ctypes.c_int(bool(onlyIfNecessary)), ctypes.byref(ierr)
                )

        @staticmethod
        def rebuildElementCache(*, onlyIfNecessary: bool = True) -> None:
            """gmsh.model.mesh.rebuildElementCache(onlyIfNecessary=True)

            Rebuild the element cache.

            Types:
            - `onlyIfNecessary`: boolean
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRebuildElementCache(
                    ctypes.c_int(bool(onlyIfNecessary)), ctypes.byref(ierr)
                )

        @staticmethod
        def getNodesForPhysicalGroup(
            dim: int, tag: int
        ) -> tuple[list[int], list[float]]:
            """gmsh.model.mesh.getNodesForPhysicalGroup(dim, tag)

            Get the nodes from all the elements belonging to the physical group of
            dimension `dim` and tag `tag`. `nodeTags` contains the node tags; `coord`
            is a vector of length 3 times the length of `nodeTags` that contains the x,
            y, z coordinates of the nodes, concatenated: [n1x, n1y, n1z, n2x, ...].

            Return `nodeTags`, `coord`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `nodeTags`: vector of sizes
            - `coord`: vector of doubles
            """
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetNodesForPhysicalGroup(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
            )

        @staticmethod
        def getMaxNodeTag() -> int:
            """gmsh.model.mesh.getMaxNodeTag()

            Get the maximum tag `maxTag` of a node in the mesh.

            Return `maxTag`.

            Types:
            - `maxTag`: size
            """
            c_maxTag = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetMaxNodeTag(
                    ctypes.byref(c_maxTag), ctypes.byref(ierr)
                )

            return c_maxTag.value

        @staticmethod
        def addNodes(
            dim: int,
            tag: int,
            nodeTags: Sequence[int],
            coord: Sequence[float],
            parametricCoord: Sequence[float] = (),
        ) -> None:
            """gmsh.model.mesh.addNodes(dim, tag, nodeTags, coord, parametricCoord=[])

            Add nodes classified on the model entity of dimension `dim` and tag `tag`.
            `nodeTags` contains the node tags (their unique, strictly positive
            identification numbers). `coord` is a vector of length 3 times the length
            of `nodeTags` that contains the x, y, z coordinates of the nodes,
            concatenated: [n1x, n1y, n1z, n2x, ...]. The optional `parametricCoord`
            vector contains the parametric coordinates of the nodes, if any. The length
            of `parametricCoord` can be 0 or `dim` times the length of `nodeTags`. If
            the `nodeTags` vector is empty, new tags are automatically assigned to the
            nodes.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `nodeTags`: vector of sizes
            - `coord`: vector of doubles
            - `parametricCoord`: vector of doubles
            """
            c_nodeTags, c_nodeTags_n = _ivectorsize(nodeTags)
            c_coord, c_coord_n = _ivectordouble(coord)
            c_parametricCoord, c_parametricCoord_n = _ivectordouble(
                parametricCoord
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAddNodes(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    c_nodeTags,
                    c_nodeTags_n,
                    c_coord,
                    c_coord_n,
                    c_parametricCoord,
                    c_parametricCoord_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def reclassifyNodes() -> None:
            """gmsh.model.mesh.reclassifyNodes()

            Reclassify all nodes on their associated model entity, based on the
            elements. Can be used when importing nodes in bulk (e.g. by associating
            them all to a single volume), to reclassify them correctly on model
            surfaces, curves, etc. after the elements have been set.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshReclassifyNodes(ctypes.byref(ierr))

        @staticmethod
        def relocateNodes(dim: int = -1, tag: int = -1) -> None:
            """gmsh.model.mesh.relocateNodes(dim=-1, tag=-1)

            Relocate the nodes classified on the entity of dimension `dim` and tag
            `tag` using their parametric coordinates. If `tag` < 0, relocate the nodes
            for all entities of dimension `dim`. If `dim` and `tag` are negative,
            relocate all the nodes in the mesh.

            Types:
            - `dim`: integer
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRelocateNodes(
                    ctypes.c_int(dim), ctypes.c_int(tag), ctypes.byref(ierr)
                )

        @staticmethod
        def getElements(
            dim: int = -1, tag: int = -1
        ) -> tuple[list[int], list[list[int]], list[list[int]]]:
            """gmsh.model.mesh.getElements(dim=-1, tag=-1)

            Get the elements classified on the entity of dimension `dim` and tag `tag`.
            If `tag` < 0, get the elements for all entities of dimension `dim`. If
            `dim` and `tag` are negative, get all the elements in the mesh.
            `elementTypes` contains the MSH types of the elements (e.g. `2` for 3-node
            triangles: see `getElementProperties` to obtain the properties for a given
            element type). `elementTags` is a vector of the same length as
            `elementTypes`; each entry is a vector containing the tags (unique,
            strictly positive identifiers) of the elements of the corresponding type.
            `nodeTags` is also a vector of the same length as `elementTypes`; each
            entry is a vector of length equal to the number of elements of the given
            type times the number N of nodes for this type of element, that contains
            the node tags of all the elements of the given type, concatenated: [e1n1,
            e1n2, ..., e1nN, e2n1, ...].

            Return `elementTypes`, `elementTags`, `nodeTags`.

            Types:
            - `elementTypes`: vector of integers
            - `elementTags`: vector of vectors of sizes
            - `nodeTags`: vector of vectors of sizes
            - `dim`: integer
            - `tag`: integer
            """
            c_elementTypes = ctypes.POINTER(ctypes.c_int)()
            c_elementTypes_n = ctypes.c_size_t()
            c_elementTags, c_elementTags_n, c_elementTags_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_size_t))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_nodeTags, c_nodeTags_n, c_nodeTags_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_size_t))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElements(
                    ctypes.byref(c_elementTypes),
                    ctypes.byref(c_elementTypes_n),
                    ctypes.byref(c_elementTags),
                    ctypes.byref(c_elementTags_n),
                    ctypes.byref(c_elementTags_nn),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_nodeTags_nn),
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorint(c_elementTypes, c_elementTypes_n.value),
                _ovectorvectorsize(
                    c_elementTags, c_elementTags_n, c_elementTags_nn
                ),
                _ovectorvectorsize(c_nodeTags, c_nodeTags_n, c_nodeTags_nn),
            )

        @staticmethod
        def getElement(elementTag: int) -> tuple[int, list[int], int, int]:
            """gmsh.model.mesh.getElement(elementTag)

            Get the type and node tags of the element with tag `tag`, as well as the
            dimension `dim` and tag `tag` of the entity on which the element is
            classified. This function relies on an internal cache (a vector in case of
            dense element numbering, a map otherwise); for large meshes accessing
            elements in bulk is often preferable.

            Return `elementType`, `nodeTags`, `dim`, `tag`.

            Types:
            - `elementTag`: size
            - `elementType`: integer
            - `nodeTags`: vector of sizes
            - `dim`: integer
            - `tag`: integer
            """
            c_elementType = ctypes.c_int()
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_dim = ctypes.c_int()
            c_tag = ctypes.c_int()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElement(
                    ctypes.c_size_t(elementTag),
                    ctypes.byref(c_elementType),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_dim),
                    ctypes.byref(c_tag),
                    ctypes.byref(ierr),
                )

            return (
                c_elementType.value,
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
                c_dim.value,
                c_tag.value,
            )

        @staticmethod
        def getElementByCoordinates(
            x: float,
            y: float,
            z: float,
            *,
            dim: int = -1,
            strict: bool = False,
        ) -> tuple[int, int, list[int], float, float, float]:
            """gmsh.model.mesh.getElementByCoordinates(x, y, z, dim=-1, strict=False)

            Search the mesh for an element located at coordinates (`x`, `y`, `z`). This
            function performs a search in a spatial octree. If an element is found,
            return its tag, type and node tags, as well as the local coordinates (`u`,
            `v`, `w`) within the reference element corresponding to search location. If
            `dim` is >= 0, only search for elements of the given dimension. If `strict`
            is not set, use a tolerance to find elements near the search location.

            Return `elementTag`, `elementType`, `nodeTags`, `u`, `v`, `w`.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `elementTag`: size
            - `elementType`: integer
            - `nodeTags`: vector of sizes
            - `u`: double
            - `v`: double
            - `w`: double
            - `dim`: integer
            - `strict`: boolean
            """
            c_elementTag = ctypes.c_size_t()
            c_elementType = ctypes.c_int()
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_u = ctypes.c_double()
            c_v = ctypes.c_double()
            c_w = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementByCoordinates(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.byref(c_elementTag),
                    ctypes.byref(c_elementType),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_u),
                    ctypes.byref(c_v),
                    ctypes.byref(c_w),
                    ctypes.c_int(dim),
                    ctypes.c_int(bool(strict)),
                    ctypes.byref(ierr),
                )

            return (
                c_elementTag.value,
                c_elementType.value,
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
                c_u.value,
                c_v.value,
                c_w.value,
            )

        @staticmethod
        def getElementsByCoordinates(
            x: float,
            y: float,
            z: float,
            *,
            dim: int = -1,
            strict: bool = False,
        ) -> list[int]:
            """gmsh.model.mesh.getElementsByCoordinates(x, y, z, dim=-1, strict=False)

            Search the mesh for element(s) located at coordinates (`x`, `y`, `z`). This
            function performs a search in a spatial octree. Return the tags of all
            found elements in `elementTags`. Additional information about the elements
            can be accessed through `getElement` and `getLocalCoordinatesInElement`. If
            `dim` is >= 0, only search for elements of the given dimension. If `strict`
            is not set, use a tolerance to find elements near the search location.

            Return `elementTags`.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `elementTags`: vector of sizes
            - `dim`: integer
            - `strict`: boolean
            """
            c_elementTags, c_elementTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementsByCoordinates(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.byref(c_elementTags),
                    ctypes.byref(c_elementTags_n),
                    ctypes.c_int(dim),
                    ctypes.c_int(bool(strict)),
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_elementTags, c_elementTags_n.value)

        @staticmethod
        def getLocalCoordinatesInElement(
            elementTag: int, x: float, y: float, z: float
        ) -> tuple[float, float, float]:
            """gmsh.model.mesh.getLocalCoordinatesInElement(elementTag, x, y, z)

            Return the local coordinates (`u`, `v`, `w`) within the element
            `elementTag` corresponding to the model coordinates (`x`, `y`, `z`). This
            function relies on an internal cache (a vector in case of dense element
            numbering, a map otherwise); for large meshes accessing elements in bulk is
            often preferable.

            Return `u`, `v`, `w`.

            Types:
            - `elementTag`: size
            - `x`: double
            - `y`: double
            - `z`: double
            - `u`: double
            - `v`: double
            - `w`: double
            """
            c_u = ctypes.c_double()
            c_v = ctypes.c_double()
            c_w = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetLocalCoordinatesInElement(
                    ctypes.c_size_t(elementTag),
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.byref(c_u),
                    ctypes.byref(c_v),
                    ctypes.byref(c_w),
                    ctypes.byref(ierr),
                )

            return (c_u.value, c_v.value, c_w.value)

        @staticmethod
        def getElementTypes(dim: int = -1, tag: int = -1) -> list[int]:
            """gmsh.model.mesh.getElementTypes(dim=-1, tag=-1)

            Get the types of elements in the entity of dimension `dim` and tag `tag`.
            If `tag` < 0, get the types for all entities of dimension `dim`. If `dim`
            and `tag` are negative, get all the types in the mesh.

            Return `elementTypes`.

            Types:
            - `elementTypes`: vector of integers
            - `dim`: integer
            - `tag`: integer
            """
            c_elementTypes = ctypes.POINTER(ctypes.c_int)()
            c_elementTypes_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementTypes(
                    ctypes.byref(c_elementTypes),
                    ctypes.byref(c_elementTypes_n),
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

            return _ovectorint(c_elementTypes, c_elementTypes_n.value)

        @staticmethod
        def getElementType(
            familyName: str, order: int, *, serendip: bool = False
        ) -> int:
            """gmsh.model.mesh.getElementType(familyName, order, serendip=False)

            Return an element type given its family name `familyName` ("Point", "Line",
            "Triangle", "Quadrangle", "Tetrahedron", "Pyramid", "Prism", "Hexahedron")
            and polynomial order `order`. If `serendip` is true, return the
            corresponding serendip element type (element without interior nodes).

            Types:
            - `familyName`: string
            - `order`: integer
            - `serendip`: boolean
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelMeshGetElementType(
                    ctypes.c_char_p(familyName.encode()),
                    ctypes.c_int(order),
                    ctypes.c_int(bool(serendip)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getElementProperties(
            elementType: int,
        ) -> tuple[str, int, int, int, list[float], int]:
            """gmsh.model.mesh.getElementProperties(elementType)

            Get the properties of an element of type `elementType`: its name
            (`elementName`), dimension (`dim`), order (`order`), number of nodes
            (`numNodes`), local coordinates of the nodes in the reference element
            (`localNodeCoord` vector, of length `dim` times `numNodes`) and number of
            primary (first order) nodes (`numPrimaryNodes`).

            Return `elementName`, `dim`, `order`, `numNodes`, `localNodeCoord`, `numPrimaryNodes`.

            Types:
            - `elementType`: integer
            - `elementName`: string
            - `dim`: integer
            - `order`: integer
            - `numNodes`: integer
            - `localNodeCoord`: vector of doubles
            - `numPrimaryNodes`: integer
            """
            c_elementName = ctypes.c_char_p()
            c_dim = ctypes.c_int()
            c_order = ctypes.c_int()
            c_numNodes = ctypes.c_int()
            c_localNodeCoord = ctypes.POINTER(ctypes.c_double)()
            c_localNodeCoord_n = ctypes.c_size_t()
            c_numPrimaryNodes = ctypes.c_int()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementProperties(
                    ctypes.c_int(elementType),
                    ctypes.byref(c_elementName),
                    ctypes.byref(c_dim),
                    ctypes.byref(c_order),
                    ctypes.byref(c_numNodes),
                    ctypes.byref(c_localNodeCoord),
                    ctypes.byref(c_localNodeCoord_n),
                    ctypes.byref(c_numPrimaryNodes),
                    ctypes.byref(ierr),
                )

            return (
                _ostring(c_elementName),
                c_dim.value,
                c_order.value,
                c_numNodes.value,
                _ovectordouble(c_localNodeCoord, c_localNodeCoord_n.value),
                c_numPrimaryNodes.value,
            )

        @staticmethod
        def getElementsByType(
            elementType: int,
            *,
            tag: int = -1,
            task: int = 0,
            numTasks: int = 1,
        ) -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.getElementsByType(elementType, tag=-1, task=0, numTasks=1)

            Get the elements of type `elementType` classified on the entity of tag
            `tag`. If `tag` < 0, get the elements for all entities. `elementTags` is a
            vector containing the tags (unique, strictly positive identifiers) of the
            elements of the corresponding type. `nodeTags` is a vector of length equal
            to the number of elements of the given type times the number N of nodes for
            this type of element, that contains the node tags of all the elements of
            the given type, concatenated: [e1n1, e1n2, ..., e1nN, e2n1, ...]. If
            `numTasks` > 1, only compute and return the part of the data indexed by
            `task` (for C++ only; output vectors must be preallocated).

            Return `elementTags`, `nodeTags`.

            Types:
            - `elementType`: integer
            - `elementTags`: vector of sizes
            - `nodeTags`: vector of sizes
            - `tag`: integer
            - `task`: size
            - `numTasks`: size
            """
            c_elementTags, c_elementTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementsByType(
                    ctypes.c_int(elementType),
                    ctypes.byref(c_elementTags),
                    ctypes.byref(c_elementTags_n),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.c_int(tag),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_elementTags, c_elementTags_n.value),
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
            )

        @staticmethod
        def getMaxElementTag() -> int:
            """gmsh.model.mesh.getMaxElementTag()

            Get the maximum tag `maxTag` of an element in the mesh.

            Return `maxTag`.

            Types:
            - `maxTag`: size
            """
            c_maxTag = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetMaxElementTag(
                    ctypes.byref(c_maxTag), ctypes.byref(ierr)
                )

            return c_maxTag.value

        @staticmethod
        def getElementQualities(
            elementTags: Sequence[int],
            *,
            qualityName: str = "minSICN",
            task: int = 0,
            numTasks: int = 1,
        ) -> list[float]:
            """gmsh.model.mesh.getElementQualities(elementTags, qualityName="minSICN", task=0, numTasks=1)

            Get the quality `elementQualities` of the elements with tags `elementTags`.
            `qualityType` is the requested quality measure: "minDetJac" and "maxDetJac"
            for the adaptively computed minimal and maximal Jacobian determinant,
            "minSJ" for the sampled minimal scaled jacobien, "minSICN" for the sampled
            minimal signed inverted condition number, "minSIGE" for the sampled signed
            inverted gradient error, "gamma" for the ratio of the inscribed to
            circumcribed sphere radius, "innerRadius" for the inner radius,
            "outerRadius" for the outerRadius, "minIsotropy" for the minimum isotropy
            measure, "angleShape" for the angle shape measure, "minEdge" for the
            minimum straight edge length, "maxEdge" for the maximum straight edge
            length, "volume" for the volume. If `numTasks` > 1, only compute and return
            the part of the data indexed by `task` (for C++ only; output vector must be
            preallocated).

            Return `elementsQuality`.

            Types:
            - `elementTags`: vector of sizes
            - `elementsQuality`: vector of doubles
            - `qualityName`: string
            - `task`: size
            - `numTasks`: size
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            c_elementsQuality = ctypes.POINTER(ctypes.c_double)()
            c_elementsQuality_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementQualities(
                    c_elementTags,
                    c_elementTags_n,
                    ctypes.byref(c_elementsQuality),
                    ctypes.byref(c_elementsQuality_n),
                    ctypes.c_char_p(qualityName.encode()),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return _ovectordouble(c_elementsQuality, c_elementsQuality_n.value)

        @staticmethod
        def addElements(
            dim: int,
            tag: int,
            elementTypes: Sequence[int],
            elementTags: Sequence[Sequence[int]],
            nodeTags: Sequence[Sequence[int]],
        ) -> None:
            """gmsh.model.mesh.addElements(dim, tag, elementTypes, elementTags, nodeTags)

            Add elements classified on the entity of dimension `dim` and tag `tag`.
            `types` contains the MSH types of the elements (e.g. `2` for 3-node
            triangles: see the Gmsh reference manual). `elementTags` is a vector of the
            same length as `types`; each entry is a vector containing the tags (unique,
            strictly positive identifiers) of the elements of the corresponding type.
            `nodeTags` is also a vector of the same length as `types`; each entry is a
            vector of length equal to the number of elements of the given type times
            the number N of nodes per element, that contains the node tags of all the
            elements of the given type, concatenated: [e1n1, e1n2, ..., e1nN, e2n1,
            ...].

            Types:
            - `dim`: integer
            - `tag`: integer
            - `elementTypes`: vector of integers
            - `elementTags`: vector of vectors of integers (size)
            - `nodeTags`: vector of vectors of integers (size)
            """
            c_elementTypes, c_elementTypes_n = _ivectorint(elementTypes)
            c_elementTags, c_elementTags_n, c_elementTags_nn = (
                _ivectorvectorsize(elementTags)
            )
            c_nodeTags, c_nodeTags_n, c_nodeTags_nn = _ivectorvectorsize(
                nodeTags
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAddElements(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    c_elementTypes,
                    c_elementTypes_n,
                    c_elementTags,
                    c_elementTags_n,
                    c_elementTags_nn,
                    c_nodeTags,
                    c_nodeTags_n,
                    c_nodeTags_nn,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addElementsByType(
            tag: int,
            elementType: int,
            elementTags: Sequence[int],
            nodeTags: Sequence[int],
        ) -> None:
            """gmsh.model.mesh.addElementsByType(tag, elementType, elementTags, nodeTags)

            Add elements of type `elementType` classified on the entity of tag `tag`.
            `elementTags` contains the tags (unique, strictly positive identifiers) of
            the elements of the corresponding type. `nodeTags` is a vector of length
            equal to the number of elements times the number N of nodes per element,
            that contains the node tags of all the elements, concatenated: [e1n1, e1n2,
            ..., e1nN, e2n1, ...]. If the `elementTag` vector is empty, new tags are
            automatically assigned to the elements.

            Types:
            - `tag`: integer
            - `elementType`: integer
            - `elementTags`: vector of sizes
            - `nodeTags`: vector of sizes
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            c_nodeTags, c_nodeTags_n = _ivectorsize(nodeTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAddElementsByType(
                    ctypes.c_int(tag),
                    ctypes.c_int(elementType),
                    c_elementTags,
                    c_elementTags_n,
                    c_nodeTags,
                    c_nodeTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getIntegrationPoints(
            elementType: int, integrationType: str
        ) -> tuple[list[float], list[float]]:
            """gmsh.model.mesh.getIntegrationPoints(elementType, integrationType)

            Get the numerical quadrature information for the given element type
            `elementType` and integration rule `integrationType`, where
            `integrationType` concatenates the integration rule family name with the
            desired order (e.g. "Gauss4" for a quadrature suited for integrating 4th
            order polynomials). The "CompositeGauss" family uses tensor-product rules
            based the 1D Gauss-Legendre rule; the "Gauss" family uses an economic
            scheme when available (i.e. with a minimal number of points), and falls
            back to "CompositeGauss" otherwise. Note that integration points for the
            "Gauss" family can fall outside of the reference element for high-order
            rules. `localCoord` contains the u, v, w coordinates of the G integration
            points in the reference element: [g1u, g1v, g1w, ..., gGu, gGv, gGw].
            `weights` contains the associated weights: [g1q, ..., gGq].

            Return `localCoord`, `weights`.

            Types:
            - `elementType`: integer
            - `integrationType`: string
            - `localCoord`: vector of doubles
            - `weights`: vector of doubles
            """
            c_localCoord = ctypes.POINTER(ctypes.c_double)()
            c_localCoord_n = ctypes.c_size_t()
            c_weights = ctypes.POINTER(ctypes.c_double)()
            c_weights_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetIntegrationPoints(
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(integrationType.encode()),
                    ctypes.byref(c_localCoord),
                    ctypes.byref(c_localCoord_n),
                    ctypes.byref(c_weights),
                    ctypes.byref(c_weights_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectordouble(c_localCoord, c_localCoord_n.value),
                _ovectordouble(c_weights, c_weights_n.value),
            )

        @staticmethod
        def getJacobians(
            elementType: int,
            localCoord: Sequence[float],
            *,
            tag: int = -1,
            task: int = 0,
            numTasks: int = 1,
        ) -> tuple[list[float], list[float], list[float]]:
            """gmsh.model.mesh.getJacobians(elementType, localCoord, tag=-1, task=0, numTasks=1)

            Get the Jacobians of all the elements of type `elementType` classified on
            the entity of tag `tag`, at the G evaluation points `localCoord` given as
            concatenated u, v, w coordinates in the reference element [g1u, g1v, g1w,
            ..., gGu, gGv, gGw]. Data is returned by element, with elements in the same
            order as in `getElements` and `getElementsByType`. `jacobians` contains for
            each element the 9 entries of the 3x3 Jacobian matrix at each evaluation
            point. The matrix is returned by column: [e1g1Jxu, e1g1Jyu, e1g1Jzu,
            e1g1Jxv, ..., e1g1Jzw, e1g2Jxu, ..., e1gGJzw, e2g1Jxu, ...], with Jxu =
            dx/du, Jyu = dy/du, etc. `determinants` contains for each element the
            determinant of the Jacobian matrix at each evaluation point: [e1g1, e1g2,
            ... e1gG, e2g1, ...]. `coord` contains for each element the x, y, z
            coordinates of the evaluation points. If `tag` < 0, get the Jacobian data
            for all entities. If `numTasks` > 1, only compute and return the part of
            the data indexed by `task` (for C++ only; output vectors must be
            preallocated).

            Return `jacobians`, `determinants`, `coord`.

            Types:
            - `elementType`: integer
            - `localCoord`: vector of doubles
            - `jacobians`: vector of doubles
            - `determinants`: vector of doubles
            - `coord`: vector of doubles
            - `tag`: integer
            - `task`: size
            - `numTasks`: size
            """
            c_localCoord, c_localCoord_n = _ivectordouble(localCoord)
            c_jacobians = ctypes.POINTER(ctypes.c_double)()
            c_jacobians_n = ctypes.c_size_t()
            c_determinants = ctypes.POINTER(ctypes.c_double)()
            c_determinants_n = ctypes.c_size_t()
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetJacobians(
                    ctypes.c_int(elementType),
                    c_localCoord,
                    c_localCoord_n,
                    ctypes.byref(c_jacobians),
                    ctypes.byref(c_jacobians_n),
                    ctypes.byref(c_determinants),
                    ctypes.byref(c_determinants_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.c_int(tag),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return (
                _ovectordouble(c_jacobians, c_jacobians_n.value),
                _ovectordouble(c_determinants, c_determinants_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
            )

        @staticmethod
        def getJacobian(
            elementTag: int, localCoord: Sequence[float]
        ) -> tuple[list[float], list[float], list[float]]:
            """gmsh.model.mesh.getJacobian(elementTag, localCoord)

            Get the Jacobian for a single element `elementTag`, at the G evaluation
            points `localCoord` given as concatenated u, v, w coordinates in the
            reference element [g1u, g1v, g1w, ..., gGu, gGv, gGw]. `jacobians` contains
            the 9 entries of the 3x3 Jacobian matrix at each evaluation point. The
            matrix is returned by column: [e1g1Jxu, e1g1Jyu, e1g1Jzu, e1g1Jxv, ...,
            e1g1Jzw, e1g2Jxu, ..., e1gGJzw, e2g1Jxu, ...], with Jxu = dx/du, Jyu =
            dy/du, etc. `determinants` contains the determinant of the Jacobian matrix
            at each evaluation point. `coord` contains the x, y, z coordinates of the
            evaluation points. This function relies on an internal cache (a vector in
            case of dense element numbering, a map otherwise); for large meshes
            accessing Jacobians in bulk is often preferable.

            Return `jacobians`, `determinants`, `coord`.

            Types:
            - `elementTag`: size
            - `localCoord`: vector of doubles
            - `jacobians`: vector of doubles
            - `determinants`: vector of doubles
            - `coord`: vector of doubles
            """
            c_localCoord, c_localCoord_n = _ivectordouble(localCoord)
            c_jacobians = ctypes.POINTER(ctypes.c_double)()
            c_jacobians_n = ctypes.c_size_t()
            c_determinants = ctypes.POINTER(ctypes.c_double)()
            c_determinants_n = ctypes.c_size_t()
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetJacobian(
                    ctypes.c_size_t(elementTag),
                    c_localCoord,
                    c_localCoord_n,
                    ctypes.byref(c_jacobians),
                    ctypes.byref(c_jacobians_n),
                    ctypes.byref(c_determinants),
                    ctypes.byref(c_determinants_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectordouble(c_jacobians, c_jacobians_n.value),
                _ovectordouble(c_determinants, c_determinants_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
            )

        @staticmethod
        def getBasisFunctions(
            elementType: int,
            localCoord: Sequence[float],
            functionSpaceType: str,
            *,
            wantedOrientations: Sequence[int] = (),
        ) -> tuple[int, list[float], int]:
            """gmsh.model.mesh.getBasisFunctions(elementType, localCoord, functionSpaceType, wantedOrientations=[])

            Get the basis functions of the element of type `elementType` at the
            evaluation points `localCoord` (given as concatenated u, v, w coordinates
            in the reference element [g1u, g1v, g1w, ..., gGu, gGv, gGw]), for the
            function space `functionSpaceType`. Currently supported function spaces
            include "Lagrange" and "GradLagrange" for isoparametric Lagrange basis
            functions and their gradient in the u, v, w coordinates of the reference
            element; "LagrangeN" and "GradLagrangeN", with N = 1, 2, ..., for N-th
            order Lagrange basis functions; "H1LegendreN" and "GradH1LegendreN", with N
            = 1, 2, ..., for N-th order hierarchical H1 Legendre functions;
            "HcurlLegendreN" and "CurlHcurlLegendreN", with N = 1, 2, ..., for N-th
            order curl-conforming basis functions. `numComponents` returns the number C
            of components of a basis function (e.g. 1 for scalar functions and 3 for
            vector functions). `basisFunctions` returns the value of the N basis
            functions at the evaluation points, i.e. [g1f1, g1f2, ..., g1fN, g2f1, ...]
            when C == 1 or [g1f1u, g1f1v, g1f1w, g1f2u, ..., g1fNw, g2f1u, ...] when C
            == 3. For basis functions that depend on the orientation of the elements,
            all values for the first orientation are returned first, followed by values
            for the second, etc. `numOrientations` returns the overall number of
            orientations. If the `wantedOrientations` vector is not empty, only return
            the values for the desired orientation indices.

            Return `numComponents`, `basisFunctions`, `numOrientations`.

            Types:
            - `elementType`: integer
            - `localCoord`: vector of doubles
            - `functionSpaceType`: string
            - `numComponents`: integer
            - `basisFunctions`: vector of doubles
            - `numOrientations`: integer
            - `wantedOrientations`: vector of integers
            """
            c_localCoord, c_localCoord_n = _ivectordouble(localCoord)
            c_numComponents = ctypes.c_int()
            c_basisFunctions = ctypes.POINTER(ctypes.c_double)()
            c_basisFunctions_n = ctypes.c_size_t()
            c_numOrientations = ctypes.c_int()
            c_wantedOrientations, c_wantedOrientations_n = _ivectorint(
                wantedOrientations
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetBasisFunctions(
                    ctypes.c_int(elementType),
                    c_localCoord,
                    c_localCoord_n,
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(c_numComponents),
                    ctypes.byref(c_basisFunctions),
                    ctypes.byref(c_basisFunctions_n),
                    ctypes.byref(c_numOrientations),
                    c_wantedOrientations,
                    c_wantedOrientations_n,
                    ctypes.byref(ierr),
                )

            return (
                c_numComponents.value,
                _ovectordouble(c_basisFunctions, c_basisFunctions_n.value),
                c_numOrientations.value,
            )

        @staticmethod
        def getBasisFunctionsOrientation(
            elementType: int,
            functionSpaceType: str,
            *,
            tag: int = -1,
            task: int = 0,
            numTasks: int = 1,
        ) -> list[int]:
            """gmsh.model.mesh.getBasisFunctionsOrientation(elementType, functionSpaceType, tag=-1, task=0, numTasks=1)

            Get the orientation index of the elements of type `elementType` in the
            entity of tag `tag`. The arguments have the same meaning as in
            `getBasisFunctions`. `basisFunctionsOrientation` is a vector giving for
            each element the orientation index in the values returned by
            `getBasisFunctions`. For Lagrange basis functions the call is superfluous
            as it will return a vector of zeros. If `numTasks` > 1, only compute and
            return the part of the data indexed by `task` (for C++ only; output vector
            must be preallocated).

            Return `basisFunctionsOrientation`.

            Types:
            - `elementType`: integer
            - `functionSpaceType`: string
            - `basisFunctionsOrientation`: vector of integers
            - `tag`: integer
            - `task`: size
            - `numTasks`: size
            """
            (c_basisFunctionsOrientation, c_basisFunctionsOrientation_n) = (
                ctypes.POINTER(ctypes.c_int)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetBasisFunctionsOrientation(
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(c_basisFunctionsOrientation),
                    ctypes.byref(c_basisFunctionsOrientation_n),
                    ctypes.c_int(tag),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return _ovectorint(
                c_basisFunctionsOrientation,
                c_basisFunctionsOrientation_n.value,
            )

        @staticmethod
        def getBasisFunctionsOrientationForElement(
            elementTag: int, functionSpaceType: str
        ) -> int:
            """gmsh.model.mesh.getBasisFunctionsOrientationForElement(elementTag, functionSpaceType)

            Get the orientation of a single element `elementTag`.

            Return `basisFunctionsOrientation`.

            Types:
            - `elementTag`: size
            - `functionSpaceType`: string
            - `basisFunctionsOrientation`: integer
            """
            c_basisFunctionsOrientation = ctypes.c_int()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetBasisFunctionsOrientationForElement(
                    ctypes.c_size_t(elementTag),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(c_basisFunctionsOrientation),
                    ctypes.byref(ierr),
                )

            return c_basisFunctionsOrientation.value

        @staticmethod
        def getNumberOfOrientations(
            elementType: int, functionSpaceType: str
        ) -> int:
            """gmsh.model.mesh.getNumberOfOrientations(elementType, functionSpaceType)

            Get the number of possible orientations for elements of type `elementType`
            and function space named `functionSpaceType`.

            Types:
            - `elementType`: integer
            - `functionSpaceType`: string
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelMeshGetNumberOfOrientations(
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getEdges(nodeTags: Sequence[int]) -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.getEdges(nodeTags)

            Get the global unique mesh edge identifiers `edgeTags` and orientations
            `edgeOrientation` for an input list of node tag pairs defining these edges,
            concatenated in the vector `nodeTags`. Mesh edges are created e.g. by
            `createEdges()', `getKeys()' or `addEdges()'. The reference positive
            orientation is n1 < n2, where n1 and n2 are the tags of the two edge nodes,
            which corresponds to the local orientation of edge-based basis functions as
            well.

            Return `edgeTags`, `edgeOrientations`.

            Types:
            - `nodeTags`: vector of sizes
            - `edgeTags`: vector of sizes
            - `edgeOrientations`: vector of integers
            """
            c_nodeTags, c_nodeTags_n = _ivectorsize(nodeTags)
            c_edgeTags, c_edgeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_edgeOrientations = ctypes.POINTER(ctypes.c_int)()
            c_edgeOrientations_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetEdges(
                    c_nodeTags,
                    c_nodeTags_n,
                    ctypes.byref(c_edgeTags),
                    ctypes.byref(c_edgeTags_n),
                    ctypes.byref(c_edgeOrientations),
                    ctypes.byref(c_edgeOrientations_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_edgeTags, c_edgeTags_n.value),
                _ovectorint(c_edgeOrientations, c_edgeOrientations_n.value),
            )

        @staticmethod
        def getFaces(
            faceType: int, nodeTags: Sequence[int]
        ) -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.getFaces(faceType, nodeTags)

            Get the global unique mesh face identifiers `faceTags` and orientations
            `faceOrientations` for an input list of a multiple of three (if `faceType`
            == 3) or four (if `faceType` == 4) node tags defining these faces,
            concatenated in the vector `nodeTags`. Mesh faces are created e.g. by
            `createFaces()', `getKeys()' or `addFaces()'.

            Return `faceTags`, `faceOrientations`.

            Types:
            - `faceType`: integer
            - `nodeTags`: vector of sizes
            - `faceTags`: vector of sizes
            - `faceOrientations`: vector of integers
            """
            c_nodeTags, c_nodeTags_n = _ivectorsize(nodeTags)
            c_faceTags, c_faceTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_faceOrientations = ctypes.POINTER(ctypes.c_int)()
            c_faceOrientations_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetFaces(
                    ctypes.c_int(faceType),
                    c_nodeTags,
                    c_nodeTags_n,
                    ctypes.byref(c_faceTags),
                    ctypes.byref(c_faceTags_n),
                    ctypes.byref(c_faceOrientations),
                    ctypes.byref(c_faceOrientations_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_faceTags, c_faceTags_n.value),
                _ovectorint(c_faceOrientations, c_faceOrientations_n.value),
            )

        @staticmethod
        def createEdges(dimTags: Sequence[tuple[int, int]] = ()) -> None:
            """gmsh.model.mesh.createEdges(dimTags=[])

            Create unique mesh edges for the entities `dimTags`, given as a vector of
            (dim, tag) pairs.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshCreateEdges(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def createFaces(dimTags: Sequence[tuple[int, int]] = ()) -> None:
            """gmsh.model.mesh.createFaces(dimTags=[])

            Create unique mesh faces for the entities `dimTags`, given as a vector of
            (dim, tag) pairs.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshCreateFaces(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def getAllEdges() -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.getAllEdges()

            Get the global unique identifiers `edgeTags` and the nodes `edgeNodes` of
            the edges in the mesh. Mesh edges are created e.g. by `createEdges()',
            `getKeys()' or addEdges().

            Return `edgeTags`, `edgeNodes`.

            Types:
            - `edgeTags`: vector of sizes
            - `edgeNodes`: vector of sizes
            """
            c_edgeTags, c_edgeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_edgeNodes, c_edgeNodes_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetAllEdges(
                    ctypes.byref(c_edgeTags),
                    ctypes.byref(c_edgeTags_n),
                    ctypes.byref(c_edgeNodes),
                    ctypes.byref(c_edgeNodes_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_edgeTags, c_edgeTags_n.value),
                _ovectorsize(c_edgeNodes, c_edgeNodes_n.value),
            )

        @staticmethod
        def getAllFaces(faceType: int) -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.getAllFaces(faceType)

            Get the global unique identifiers `faceTags` and the nodes `faceNodes` of
            the faces of type `faceType` in the mesh. Mesh faces are created e.g. by
            `createFaces()', `getKeys()' or addFaces().

            Return `faceTags`, `faceNodes`.

            Types:
            - `faceType`: integer
            - `faceTags`: vector of sizes
            - `faceNodes`: vector of sizes
            """
            c_faceTags, c_faceTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_faceNodes, c_faceNodes_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetAllFaces(
                    ctypes.c_int(faceType),
                    ctypes.byref(c_faceTags),
                    ctypes.byref(c_faceTags_n),
                    ctypes.byref(c_faceNodes),
                    ctypes.byref(c_faceNodes_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_faceTags, c_faceTags_n.value),
                _ovectorsize(c_faceNodes, c_faceNodes_n.value),
            )

        @staticmethod
        def addEdges(
            edgeTags: Sequence[int], edgeNodes: Sequence[int]
        ) -> None:
            """gmsh.model.mesh.addEdges(edgeTags, edgeNodes)

            Add mesh edges defined by their global unique identifiers `edgeTags` and
            their nodes `edgeNodes`.

            Types:
            - `edgeTags`: vector of sizes
            - `edgeNodes`: vector of sizes
            """
            c_edgeTags, c_edgeTags_n = _ivectorsize(edgeTags)
            c_edgeNodes, c_edgeNodes_n = _ivectorsize(edgeNodes)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAddEdges(
                    c_edgeTags,
                    c_edgeTags_n,
                    c_edgeNodes,
                    c_edgeNodes_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addFaces(
            faceType: int, faceTags: Sequence[int], faceNodes: Sequence[int]
        ) -> None:
            """gmsh.model.mesh.addFaces(faceType, faceTags, faceNodes)

            Add mesh faces of type `faceType` defined by their global unique
            identifiers `faceTags` and their nodes `faceNodes`.

            Types:
            - `faceType`: integer
            - `faceTags`: vector of sizes
            - `faceNodes`: vector of sizes
            """
            c_faceTags, c_faceTags_n = _ivectorsize(faceTags)
            c_faceNodes, c_faceNodes_n = _ivectorsize(faceNodes)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAddFaces(
                    ctypes.c_int(faceType),
                    c_faceTags,
                    c_faceTags_n,
                    c_faceNodes,
                    c_faceNodes_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getKeys(
            elementType: int,
            functionSpaceType: str,
            *,
            tag: int = -1,
            returnCoord: bool = True,
        ) -> tuple[list[int], list[int], list[float]]:
            """gmsh.model.mesh.getKeys(elementType, functionSpaceType, tag=-1, returnCoord=True)

            Generate the pair of keys for the elements of type `elementType` in the
            entity of tag `tag`, for the `functionSpaceType` function space. Each pair
            (`typeKey`, `entityKey`) uniquely identifies a basis function in the
            function space. If `returnCoord` is set, the `coord` vector contains the x,
            y, z coordinates locating basis functions for sorting purposes. Warning:
            this is an experimental feature and will probably change in a future
            release.

            Return `typeKeys`, `entityKeys`, `coord`.

            Types:
            - `elementType`: integer
            - `functionSpaceType`: string
            - `typeKeys`: vector of integers
            - `entityKeys`: vector of sizes
            - `coord`: vector of doubles
            - `tag`: integer
            - `returnCoord`: boolean
            """
            c_typeKeys = ctypes.POINTER(ctypes.c_int)()
            c_typeKeys_n = ctypes.c_size_t()
            c_entityKeys, c_entityKeys_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetKeys(
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(c_typeKeys),
                    ctypes.byref(c_typeKeys_n),
                    ctypes.byref(c_entityKeys),
                    ctypes.byref(c_entityKeys_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(returnCoord)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorint(c_typeKeys, c_typeKeys_n.value),
                _ovectorsize(c_entityKeys, c_entityKeys_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
            )

        @staticmethod
        def getKeysForElement(
            elementTag: int,
            functionSpaceType: str,
            *,
            returnCoord: bool = True,
        ) -> tuple[list[int], list[int], list[float]]:
            """gmsh.model.mesh.getKeysForElement(elementTag, functionSpaceType, returnCoord=True)

            Get the pair of keys for a single element `elementTag`.

            Return `typeKeys`, `entityKeys`, `coord`.

            Types:
            - `elementTag`: size
            - `functionSpaceType`: string
            - `typeKeys`: vector of integers
            - `entityKeys`: vector of sizes
            - `coord`: vector of doubles
            - `returnCoord`: boolean
            """
            c_typeKeys = ctypes.POINTER(ctypes.c_int)()
            c_typeKeys_n = ctypes.c_size_t()
            c_entityKeys, c_entityKeys_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetKeysForElement(
                    ctypes.c_size_t(elementTag),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(c_typeKeys),
                    ctypes.byref(c_typeKeys_n),
                    ctypes.byref(c_entityKeys),
                    ctypes.byref(c_entityKeys_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.c_int(bool(returnCoord)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorint(c_typeKeys, c_typeKeys_n.value),
                _ovectorsize(c_entityKeys, c_entityKeys_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
            )

        @staticmethod
        def getNumberOfKeys(elementType: int, functionSpaceType: str) -> int:
            """gmsh.model.mesh.getNumberOfKeys(elementType, functionSpaceType)

            Get the number of keys by elements of type `elementType` for function space
            named `functionSpaceType`.

            Types:
            - `elementType`: integer
            - `functionSpaceType`: string
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelMeshGetNumberOfKeys(
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getKeysInformation(
            typeKeys: Sequence[int],
            entityKeys: Sequence[int],
            elementType: int,
            functionSpaceType: str,
        ) -> list[tuple[int, int]]:
            """gmsh.model.mesh.getKeysInformation(typeKeys, entityKeys, elementType, functionSpaceType)

            Get information about the pair of `keys`. `infoKeys` returns information
            about the functions associated with the pairs (`typeKeys`, `entityKey`).
            `infoKeys[0].first' describes the type of function (0 for  vertex function,
            1 for edge function, 2 for face function and 3 for bubble function).
            `infoKeys[0].second' gives the order of the function associated with the
            key. Warning: this is an experimental feature and will probably change in a
            future release.

            Return `infoKeys`.

            Types:
            - `typeKeys`: vector of integers
            - `entityKeys`: vector of sizes
            - `elementType`: integer
            - `functionSpaceType`: string
            - `infoKeys`: vector of pairs of integers
            """
            c_typeKeys, c_typeKeys_n = _ivectorint(typeKeys)
            c_entityKeys, c_entityKeys_n = _ivectorsize(entityKeys)
            c_infoKeys = ctypes.POINTER(ctypes.c_int)()
            c_infoKeys_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetKeysInformation(
                    c_typeKeys,
                    c_typeKeys_n,
                    c_entityKeys,
                    c_entityKeys_n,
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.byref(c_infoKeys),
                    ctypes.byref(c_infoKeys_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_infoKeys, c_infoKeys_n.value)

        @staticmethod
        def getBarycenters(
            elementType: int,
            tag: int,
            *,
            fast: bool,
            primary: bool,
            task: int = 0,
            numTasks: int = 1,
        ) -> list[float]:
            """gmsh.model.mesh.getBarycenters(elementType, tag, fast, primary, task=0, numTasks=1)

            Get the barycenters of all elements of type `elementType` classified on the
            entity of tag `tag`. If `primary` is set, only the primary nodes of the
            elements are taken into account for the barycenter calculation. If `fast`
            is set, the function returns the sum of the primary node coordinates
            (without normalizing by the number of nodes). If `tag` < 0, get the
            barycenters for all entities. If `numTasks` > 1, only compute and return
            the part of the data indexed by `task` (for C++ only; output vector must be
            preallocated).

            Return `barycenters`.

            Types:
            - `elementType`: integer
            - `tag`: integer
            - `fast`: boolean
            - `primary`: boolean
            - `barycenters`: vector of doubles
            - `task`: size
            - `numTasks`: size
            """
            c_barycenters = ctypes.POINTER(ctypes.c_double)()
            c_barycenters_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetBarycenters(
                    ctypes.c_int(elementType),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(fast)),
                    ctypes.c_int(bool(primary)),
                    ctypes.byref(c_barycenters),
                    ctypes.byref(c_barycenters_n),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return _ovectordouble(c_barycenters, c_barycenters_n.value)

        @staticmethod
        def getElementEdgeNodes(
            elementType: int,
            *,
            tag: int = -1,
            primary: bool = False,
            task: int = 0,
            numTasks: int = 1,
        ) -> list[int]:
            """gmsh.model.mesh.getElementEdgeNodes(elementType, tag=-1, primary=False, task=0, numTasks=1)

            Get the nodes on the edges of all elements of type `elementType` classified
            on the entity of tag `tag`. `nodeTags` contains the node tags of the edges
            for all the elements: [e1a1n1, e1a1n2, e1a2n1, ...]. Data is returned by
            element, with elements in the same order as in `getElements` and
            `getElementsByType`. If `primary` is set, only the primary (begin/end)
            nodes of the edges are returned. If `tag` < 0, get the edge nodes for all
            entities. If `numTasks` > 1, only compute and return the part of the data
            indexed by `task` (for C++ only; output vector must be preallocated).

            Return `nodeTags`.

            Types:
            - `elementType`: integer
            - `nodeTags`: vector of sizes
            - `tag`: integer
            - `primary`: boolean
            - `task`: size
            - `numTasks`: size
            """
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementEdgeNodes(
                    ctypes.c_int(elementType),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(primary)),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_nodeTags, c_nodeTags_n.value)

        @staticmethod
        def getElementFaceNodes(
            elementType: int,
            faceType: int,
            *,
            tag: int = -1,
            primary: bool = False,
            task: int = 0,
            numTasks: int = 1,
        ) -> list[int]:
            """gmsh.model.mesh.getElementFaceNodes(elementType, faceType, tag=-1, primary=False, task=0, numTasks=1)

            Get the nodes on the faces of type `faceType` (3 for triangular faces, 4
            for quadrangular faces) of all elements of type `elementType` classified on
            the entity of tag `tag`. `nodeTags` contains the node tags of the faces for
            all elements: [e1f1n1, ..., e1f1nFaceType, e1f2n1, ...]. Data is returned
            by element, with elements in the same order as in `getElements` and
            `getElementsByType`. If `primary` is set, only the primary (corner) nodes
            of the faces are returned. If `tag` < 0, get the face nodes for all
            entities. If `numTasks` > 1, only compute and return the part of the data
            indexed by `task` (for C++ only; output vector must be preallocated).

            Return `nodeTags`.

            Types:
            - `elementType`: integer
            - `faceType`: integer
            - `nodeTags`: vector of sizes
            - `tag`: integer
            - `primary`: boolean
            - `task`: size
            - `numTasks`: size
            """
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetElementFaceNodes(
                    ctypes.c_int(elementType),
                    ctypes.c_int(faceType),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(primary)),
                    ctypes.c_size_t(task),
                    ctypes.c_size_t(numTasks),
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_nodeTags, c_nodeTags_n.value)

        @staticmethod
        def getGhostElements(
            dim: int, tag: int
        ) -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.getGhostElements(dim, tag)

            Get the ghost elements `elementTags` and their associated `partitions`
            stored in the ghost entity of dimension `dim` and tag `tag`.

            Return `elementTags`, `partitions`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `elementTags`: vector of sizes
            - `partitions`: vector of integers
            """
            c_elementTags, c_elementTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_partitions = ctypes.POINTER(ctypes.c_int)()
            c_partitions_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetGhostElements(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_elementTags),
                    ctypes.byref(c_elementTags_n),
                    ctypes.byref(c_partitions),
                    ctypes.byref(c_partitions_n),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_elementTags, c_elementTags_n.value),
                _ovectorint(c_partitions, c_partitions_n.value),
            )

        @staticmethod
        def setSize(dimTags: Sequence[tuple[int, int]], size: float) -> None:
            """gmsh.model.mesh.setSize(dimTags, size)

            Set a mesh size constraint on the model entities `dimTags`, given as a
            vector of (dim, tag) pairs. Currently only entities of dimension 0 (points)
            are handled.

            Types:
            - `dimTags`: vector of pairs of integers
            - `size`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetSize(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(size),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getSizes(dimTags: Sequence[tuple[int, int]]) -> list[float]:
            """gmsh.model.mesh.getSizes(dimTags)

            Get the mesh size constraints (if any) associated with the model entities
            `dimTags`, given as a vector of (dim, tag) pairs. A zero entry in the
            output `sizes` vector indicates that no size constraint is specified on the
            corresponding entity.

            Return `sizes`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `sizes`: vector of doubles
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_sizes = ctypes.POINTER(ctypes.c_double)()
            c_sizes_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetSizes(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(c_sizes),
                    ctypes.byref(c_sizes_n),
                    ctypes.byref(ierr),
                )

            return _ovectordouble(c_sizes, c_sizes_n.value)

        @staticmethod
        def setSizeAtParametricPoints(
            dim: int,
            tag: int,
            parametricCoord: Sequence[float],
            sizes: Sequence[float],
        ) -> None:
            """gmsh.model.mesh.setSizeAtParametricPoints(dim, tag, parametricCoord, sizes)

            Set mesh size constraints at the given parametric points `parametricCoord`
            on the model entity of dimension `dim` and tag `tag`. Currently only
            entities of dimension 1 (lines) are handled.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `parametricCoord`: vector of doubles
            - `sizes`: vector of doubles
            """
            c_parametricCoord, c_parametricCoord_n = _ivectordouble(
                parametricCoord
            )
            c_sizes, c_sizes_n = _ivectordouble(sizes)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetSizeAtParametricPoints(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    c_parametricCoord,
                    c_parametricCoord_n,
                    c_sizes,
                    c_sizes_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setSizeCallback(
            callback: Callable[[int, int, float, float, float, float], None],
        ) -> None:
            """gmsh.model.mesh.setSizeCallback(callback)

            Set a mesh size callback for the current model. The callback function
            should take six arguments as input (`dim`, `tag`, `x`, `y`, `z` and `lc`).
            The first two integer arguments correspond to the dimension `dim` and tag
            `tag` of the entity being meshed. The next four double precision arguments
            correspond to the coordinates `x`, `y` and `z` around which to prescribe
            the mesh size and to the mesh size `lc` that would be prescribed if the
            callback had not been called. The callback function should return a double
            precision number specifying the desired mesh size; returning `lc` is
            equivalent to a no-op.

            Types:
            - `callback`:
            """
            # TODO: tidy this global mutation?
            #   https://github.com/Rupt/tmsh/issues/14
            gmsh.c_callback_type = ctypes.CFUNCTYPE(
                ctypes.c_double,
                ctypes.c_int,
                ctypes.c_int,
                ctypes.c_double,
                ctypes.c_double,
                ctypes.c_double,
                ctypes.c_double,
                ctypes.c_void_p,
            )
            gmsh.c_callback = gmsh.c_callback_type(
                lambda dim, tag, x, y, z, lc, _: callback(
                    dim, tag, x, y, z, lc
                )
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetSizeCallback(
                    gmsh.c_callback, None, ctypes.byref(ierr)
                )

        @staticmethod
        def removeSizeCallback() -> None:
            """gmsh.model.mesh.removeSizeCallback()

            Remove the mesh size callback from the current model.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRemoveSizeCallback(ctypes.byref(ierr))

        @staticmethod
        def setTransfiniteCurve(
            tag: int,
            numNodes: int,
            *,
            meshType: str = "Progression",
            coef: float = 1.0,
        ) -> None:
            """gmsh.model.mesh.setTransfiniteCurve(tag, numNodes, meshType="Progression", coef=1.)

            Set a transfinite meshing constraint on the curve `tag`, with `numNodes`
            nodes distributed according to `meshType` and `coef`. Currently supported
            types are "Progression" (geometrical progression with power `coef`), "Bump"
            (refinement toward both extremities of the curve) and "Beta" (beta law).

            Types:
            - `tag`: integer
            - `numNodes`: integer
            - `meshType`: string
            - `coef`: double
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetTransfiniteCurve(
                    ctypes.c_int(tag),
                    ctypes.c_int(numNodes),
                    ctypes.c_char_p(meshType.encode()),
                    ctypes.c_double(coef),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setTransfiniteSurface(
            tag: int,
            *,
            arrangement: str = "Left",
            cornerTags: Sequence[int] = (),
        ) -> None:
            """gmsh.model.mesh.setTransfiniteSurface(tag, arrangement="Left", cornerTags=[])

            Set a transfinite meshing constraint on the surface `tag`. `arrangement`
            describes the arrangement of the triangles when the surface is not flagged
            as recombined: currently supported values are "Left", "Right",
            "AlternateLeft" and "AlternateRight". `cornerTags` can be used to specify
            the (3 or 4) corners of the transfinite interpolation explicitly;
            specifying the corners explicitly is mandatory if the surface has more that
            3 or 4 points on its boundary.

            Types:
            - `tag`: integer
            - `arrangement`: string
            - `cornerTags`: vector of integers
            """
            c_cornerTags, c_cornerTags_n = _ivectorint(cornerTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetTransfiniteSurface(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(arrangement.encode()),
                    c_cornerTags,
                    c_cornerTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setTransfiniteVolume(
            tag: int, *, cornerTags: Sequence[int] = ()
        ) -> None:
            """gmsh.model.mesh.setTransfiniteVolume(tag, cornerTags=[])

            Set a transfinite meshing constraint on the surface `tag`. `cornerTags` can
            be used to specify the (6 or 8) corners of the transfinite interpolation
            explicitly.

            Types:
            - `tag`: integer
            - `cornerTags`: vector of integers
            """
            c_cornerTags, c_cornerTags_n = _ivectorint(cornerTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetTransfiniteVolume(
                    ctypes.c_int(tag),
                    c_cornerTags,
                    c_cornerTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setTransfiniteAutomatic(
            dimTags: Sequence[tuple[int, int]] = (),
            *,
            cornerAngle: float = 2.35,
            recombine: bool = True,
        ) -> None:
            """gmsh.model.mesh.setTransfiniteAutomatic(dimTags=[], cornerAngle=2.35, recombine=True)

            Set transfinite meshing constraints on the model entities in `dimTags`,
            given as a vector of (dim, tag) pairs. Transfinite meshing constraints are
            added to the curves of the quadrangular surfaces and to the faces of
            6-sided volumes. Quadragular faces with a corner angle superior to
            `cornerAngle` (in radians) are ignored. The number of points is
            automatically determined from the sizing constraints. If `dimTag` is empty,
            the constraints are applied to all entities in the model. If `recombine` is
            true, the recombine flag is automatically set on the transfinite surfaces.

            Types:
            - `dimTags`: vector of pairs of integers
            - `cornerAngle`: double
            - `recombine`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetTransfiniteAutomatic(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(cornerAngle),
                    ctypes.c_int(bool(recombine)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setRecombine(dim: int, tag: int, *, angle: float = 45.0) -> None:
            """gmsh.model.mesh.setRecombine(dim, tag, angle=45.)

            Set a recombination meshing constraint on the model entity of dimension
            `dim` and tag `tag`. Currently only entities of dimension 2 (to recombine
            triangles into quadrangles) are supported; `angle` specifies the threshold
            angle for the simple recombination algorithm..

            Types:
            - `dim`: integer
            - `tag`: integer
            - `angle`: double
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetRecombine(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setSmoothing(dim: int, tag: int, val: int) -> None:
            """gmsh.model.mesh.setSmoothing(dim, tag, val)

            Set a smoothing meshing constraint on the model entity of dimension `dim`
            and tag `tag`. `val` iterations of a Laplace smoother are applied.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `val`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetSmoothing(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.c_int(val),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setReverse(dim: int, tag: int, val: bool = True) -> None:  # noqa: FBT001 FBT002
            """gmsh.model.mesh.setReverse(dim, tag, val=True)

            Set a reverse meshing constraint on the model entity of dimension `dim` and
            tag `tag`. If `val` is true, the mesh orientation will be reversed with
            respect to the natural mesh orientation (i.e. the orientation consistent
            with the orientation of the geometry). If `val` is false, the mesh is left
            as-is.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `val`: boolean
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetReverse(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(val)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setAlgorithm(dim: int, tag: int, val: int) -> None:
            """gmsh.model.mesh.setAlgorithm(dim, tag, val)

            Set the meshing algorithm on the model entity of dimension `dim` and tag
            `tag`. Supported values are those of the `Mesh.Algorithm' option, as listed
            in the Gmsh reference manual. Currently only supported for `dim` == 2.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `val`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetAlgorithm(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.c_int(val),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setSizeFromBoundary(dim: int, tag: int, val: int) -> None:
            """gmsh.model.mesh.setSizeFromBoundary(dim, tag, val)

            Force the mesh size to be extended from the boundary, or not, for the model
            entity of dimension `dim` and tag `tag`. Currently only supported for `dim`
            == 2.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `val`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetSizeFromBoundary(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.c_int(val),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setCompound(dim: int, tags: Sequence[int]) -> None:
            """gmsh.model.mesh.setCompound(dim, tags)

            Set a compound meshing constraint on the model entities of dimension `dim`
            and tags `tags`. During meshing, compound entities are treated as a single
            discrete entity, which is automatically reparametrized.

            Types:
            - `dim`: integer
            - `tags`: vector of integers
            """
            c_tags, c_tags_n = _ivectorint(tags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetCompound(
                    ctypes.c_int(dim), c_tags, c_tags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def setOutwardOrientation(tag: int) -> None:
            """gmsh.model.mesh.setOutwardOrientation(tag)

            Set meshing constraints on the bounding surfaces of the volume of tag `tag`
            so that all surfaces are oriented with outward pointing normals; and if a
            mesh already exists, reorient it. Currently only available with the
            OpenCASCADE kernel, as it relies on the STL triangulation.

            Types:
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetOutwardOrientation(
                    ctypes.c_int(tag), ctypes.byref(ierr)
                )

        @staticmethod
        def removeConstraints(dimTags: Sequence[tuple[int, int]] = ()) -> None:
            """gmsh.model.mesh.removeConstraints(dimTags=[])

            Remove all meshing constraints from the model entities `dimTags`, given as
            a vector of (dim, tag) pairs. If `dimTags` is empty, remove all
            constraings.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRemoveConstraints(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def embed(
            dim: int, tags: Sequence[int], inDim: int, inTag: int
        ) -> None:
            """gmsh.model.mesh.embed(dim, tags, inDim, inTag)

            Embed the model entities of dimension `dim` and tags `tags` in the
            (`inDim`, `inTag`) model entity. The dimension `dim` can 0, 1 or 2 and must
            be strictly smaller than `inDim`, which must be either 2 or 3. The embedded
            entities should not intersect each other or be part of the boundary of the
            entity `inTag`, whose mesh will conform to the mesh of the embedded
            entities. With the OpenCASCADE kernel, if the `fragment` operation is
            applied to entities of different dimensions, the lower dimensional entities
            will be automatically embedded in the higher dimensional entities if they
            are not on their boundary.

            Types:
            - `dim`: integer
            - `tags`: vector of integers
            - `inDim`: integer
            - `inTag`: integer
            """
            c_tags, c_tags_n = _ivectorint(tags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshEmbed(
                    ctypes.c_int(dim),
                    c_tags,
                    c_tags_n,
                    ctypes.c_int(inDim),
                    ctypes.c_int(inTag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def removeEmbedded(
            dimTags: Sequence[tuple[int, int]], *, dim: int = -1
        ) -> None:
            """gmsh.model.mesh.removeEmbedded(dimTags, dim=-1)

            Remove embedded entities from the model entities `dimTags`, given as a
            vector of (dim, tag) pairs. if `dim` is >= 0, only remove embedded entities
            of the given dimension (e.g. embedded points if `dim` == 0).

            Types:
            - `dimTags`: vector of pairs of integers
            - `dim`: integer
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRemoveEmbedded(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_int(dim),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getEmbedded(dim: int, tag: int) -> list[tuple[int, int]]:
            """gmsh.model.mesh.getEmbedded(dim, tag)

            Get the entities (if any) embedded in the model entity of dimension `dim`
            and tag `tag`.

            Return `dimTags`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags = ctypes.POINTER(ctypes.c_int)()
            c_dimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetEmbedded(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_dimTags),
                    ctypes.byref(c_dimTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_dimTags, c_dimTags_n.value)

        @staticmethod
        def reorderElements(
            elementType: int, tag: int, ordering: Sequence[int]
        ) -> None:
            """gmsh.model.mesh.reorderElements(elementType, tag, ordering)

            Reorder the elements of type `elementType` classified on the entity of tag
            `tag` according to the `ordering` vector.

            Types:
            - `elementType`: integer
            - `tag`: integer
            - `ordering`: vector of sizes
            """
            c_ordering, c_ordering_n = _ivectorsize(ordering)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshReorderElements(
                    ctypes.c_int(elementType),
                    ctypes.c_int(tag),
                    c_ordering,
                    c_ordering_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def computeRenumbering(
            method: str = "RCMK", elementTags: Sequence[int] = ()
        ) -> tuple[list[int], list[int]]:
            """gmsh.model.mesh.computeRenumbering(method="RCMK", elementTags=[])

            Compute a renumbering vector `newTags` corresponding to the input tags
            `oldTags` for a given list of element tags `elementTags`. If `elementTags`
            is empty, compute the renumbering on the full mesh. If `method` is equal to
            "RCMK", compute a node renumering with Reverse Cuthill McKee. If `method`
            is equal to "Hilbert", compute a node renumering along a Hilbert curve. If
            `method` is equal to "Metis", compute a node renumering using Metis.
            Element renumbering is not available yet.

            Return `oldTags`, `newTags`.

            Types:
            - `oldTags`: vector of sizes
            - `newTags`: vector of sizes
            - `method`: string
            - `elementTags`: vector of sizes
            """
            c_oldTags, c_oldTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_newTags, c_newTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshComputeRenumbering(
                    ctypes.byref(c_oldTags),
                    ctypes.byref(c_oldTags_n),
                    ctypes.byref(c_newTags),
                    ctypes.byref(c_newTags_n),
                    ctypes.c_char_p(method.encode()),
                    c_elementTags,
                    c_elementTags_n,
                    ctypes.byref(ierr),
                )

            return (
                _ovectorsize(c_oldTags, c_oldTags_n.value),
                _ovectorsize(c_newTags, c_newTags_n.value),
            )

        @staticmethod
        def renumberNodes(
            oldTags: Sequence[int] = [], newTags: Sequence[int] = ()
        ) -> None:
            """gmsh.model.mesh.renumberNodes(oldTags=[], newTags=[])

            Renumber the node tags. If no explicit renumbering is provided through the
            `oldTags` and `newTags` vectors, renumber the nodes in a continuous
            sequence, taking into account the subset of elements to be saved later on
            if the option "Mesh.SaveAll" is not set.

            Types:
            - `oldTags`: vector of sizes
            - `newTags`: vector of sizes
            """
            c_oldTags, c_oldTags_n = _ivectorsize(oldTags)
            c_newTags, c_newTags_n = _ivectorsize(newTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRenumberNodes(
                    c_oldTags,
                    c_oldTags_n,
                    c_newTags,
                    c_newTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def renumberElements(
            oldTags: Sequence[int] = [], newTags: Sequence[int] = ()
        ) -> None:
            """gmsh.model.mesh.renumberElements(oldTags=[], newTags=[])

            Renumber the element tags in a continuous sequence. If no explicit
            renumbering is provided through the `oldTags` and `newTags` vectors,
            renumber the elements in a continuous sequence, taking into account the
            subset of elements to be saved later on if the option "Mesh.SaveAll" is not
            set.

            Types:
            - `oldTags`: vector of sizes
            - `newTags`: vector of sizes
            """
            c_oldTags, c_oldTags_n = _ivectorsize(oldTags)
            c_newTags, c_newTags_n = _ivectorsize(newTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRenumberElements(
                    c_oldTags,
                    c_oldTags_n,
                    c_newTags,
                    c_newTags_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setPeriodic(
            dim: int,
            tags: Sequence[int],
            tagsMaster: Sequence[int],
            affineTransform: Sequence[float],
        ) -> None:
            """gmsh.model.mesh.setPeriodic(dim, tags, tagsMaster, affineTransform)

            Set the meshes of the entities of dimension `dim` and tag `tags` as
            periodic copies of the meshes of entities `tagsMaster`, using the affine
            transformation specified in `affineTransformation` (16 entries of a 4x4
            matrix, by row). If used after meshing, generate the periodic node
            correspondence information assuming the meshes of entities `tags`
            effectively match the meshes of entities `tagsMaster` (useful for
            structured and extruded meshes). Currently only available for @code{dim} ==
            1 and @code{dim} == 2.

            Types:
            - `dim`: integer
            - `tags`: vector of integers
            - `tagsMaster`: vector of integers
            - `affineTransform`: vector of doubles
            """
            c_tags, c_tags_n = _ivectorint(tags)
            c_tagsMaster, c_tagsMaster_n = _ivectorint(tagsMaster)
            c_affineTransform, c_affineTransform_n = _ivectordouble(
                affineTransform
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetPeriodic(
                    ctypes.c_int(dim),
                    c_tags,
                    c_tags_n,
                    c_tagsMaster,
                    c_tagsMaster_n,
                    c_affineTransform,
                    c_affineTransform_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getPeriodic(dim: int, tags: Sequence[int]) -> list[int]:
            """gmsh.model.mesh.getPeriodic(dim, tags)

            Get master entities `tagsMaster` for the entities of dimension `dim` and
            tags `tags`.

            Return `tagMaster`.

            Types:
            - `dim`: integer
            - `tags`: vector of integers
            - `tagMaster`: vector of integers
            """
            c_tags, c_tags_n = _ivectorint(tags)
            c_tagMaster = ctypes.POINTER(ctypes.c_int)()
            c_tagMaster_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetPeriodic(
                    ctypes.c_int(dim),
                    c_tags,
                    c_tags_n,
                    ctypes.byref(c_tagMaster),
                    ctypes.byref(c_tagMaster_n),
                    ctypes.byref(ierr),
                )

            return _ovectorint(c_tagMaster, c_tagMaster_n.value)

        @staticmethod
        def getPeriodicNodes(
            dim: int, tag: int, *, includeHighOrderNodes: bool = False
        ) -> tuple[int, list[int], list[int], list[float]]:
            """gmsh.model.mesh.getPeriodicNodes(dim, tag, includeHighOrderNodes=False)

            Get the master entity `tagMaster`, the node tags `nodeTags` and their
            corresponding master node tags `nodeTagsMaster`, and the affine transform
            `affineTransform` for the entity of dimension `dim` and tag `tag`. If
            `includeHighOrderNodes` is set, include high-order nodes in the returned
            data.

            Return `tagMaster`, `nodeTags`, `nodeTagsMaster`, `affineTransform`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `tagMaster`: integer
            - `nodeTags`: vector of sizes
            - `nodeTagsMaster`: vector of sizes
            - `affineTransform`: vector of doubles
            - `includeHighOrderNodes`: boolean
            """
            c_tagMaster = ctypes.c_int()
            c_nodeTags, c_nodeTags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_nodeTagsMaster, c_nodeTagsMaster_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_affineTransform = ctypes.POINTER(ctypes.c_double)()
            c_affineTransform_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetPeriodicNodes(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_tagMaster),
                    ctypes.byref(c_nodeTags),
                    ctypes.byref(c_nodeTags_n),
                    ctypes.byref(c_nodeTagsMaster),
                    ctypes.byref(c_nodeTagsMaster_n),
                    ctypes.byref(c_affineTransform),
                    ctypes.byref(c_affineTransform_n),
                    ctypes.c_int(bool(includeHighOrderNodes)),
                    ctypes.byref(ierr),
                )

            return (
                c_tagMaster.value,
                _ovectorsize(c_nodeTags, c_nodeTags_n.value),
                _ovectorsize(c_nodeTagsMaster, c_nodeTagsMaster_n.value),
                _ovectordouble(c_affineTransform, c_affineTransform_n.value),
            )

        @staticmethod
        def getPeriodicKeys(
            elementType: int,
            functionSpaceType: str,
            tag: int,
            *,
            returnCoord: bool = True,
        ) -> tuple[
            int,
            list[int],
            list[int],
            list[int],
            list[int],
            list[float],
            list[float],
        ]:
            """gmsh.model.mesh.getPeriodicKeys(elementType, functionSpaceType, tag, returnCoord=True)

            Get the master entity `tagMaster` and the key pairs (`typeKeyMaster`,
            `entityKeyMaster`) corresponding to the entity `tag` and the key pairs
            (`typeKey`, `entityKey`) for the elements of type `elementType` and
            function space type `functionSpaceType`. If `returnCoord` is set, the
            `coord` and `coordMaster` vectors contain the x, y, z coordinates locating
            basis functions for sorting purposes.

            Return `tagMaster`, `typeKeys`, `typeKeysMaster`, `entityKeys`, `entityKeysMaster`, `coord`, `coordMaster`.

            Types:
            - `elementType`: integer
            - `functionSpaceType`: string
            - `tag`: integer
            - `tagMaster`: integer
            - `typeKeys`: vector of integers
            - `typeKeysMaster`: vector of integers
            - `entityKeys`: vector of sizes
            - `entityKeysMaster`: vector of sizes
            - `coord`: vector of doubles
            - `coordMaster`: vector of doubles
            - `returnCoord`: boolean
            """
            c_tagMaster = ctypes.c_int()
            c_typeKeys = ctypes.POINTER(ctypes.c_int)()
            c_typeKeys_n = ctypes.c_size_t()
            c_typeKeysMaster = ctypes.POINTER(ctypes.c_int)()
            c_typeKeysMaster_n = ctypes.c_size_t()
            c_entityKeys, c_entityKeys_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_entityKeysMaster, c_entityKeysMaster_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_coord = ctypes.POINTER(ctypes.c_double)()
            c_coord_n = ctypes.c_size_t()
            c_coordMaster = ctypes.POINTER(ctypes.c_double)()
            c_coordMaster_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetPeriodicKeys(
                    ctypes.c_int(elementType),
                    ctypes.c_char_p(functionSpaceType.encode()),
                    ctypes.c_int(tag),
                    ctypes.byref(c_tagMaster),
                    ctypes.byref(c_typeKeys),
                    ctypes.byref(c_typeKeys_n),
                    ctypes.byref(c_typeKeysMaster),
                    ctypes.byref(c_typeKeysMaster_n),
                    ctypes.byref(c_entityKeys),
                    ctypes.byref(c_entityKeys_n),
                    ctypes.byref(c_entityKeysMaster),
                    ctypes.byref(c_entityKeysMaster_n),
                    ctypes.byref(c_coord),
                    ctypes.byref(c_coord_n),
                    ctypes.byref(c_coordMaster),
                    ctypes.byref(c_coordMaster_n),
                    ctypes.c_int(bool(returnCoord)),
                    ctypes.byref(ierr),
                )

            return (
                c_tagMaster.value,
                _ovectorint(c_typeKeys, c_typeKeys_n.value),
                _ovectorint(c_typeKeysMaster, c_typeKeysMaster_n.value),
                _ovectorsize(c_entityKeys, c_entityKeys_n.value),
                _ovectorsize(c_entityKeysMaster, c_entityKeysMaster_n.value),
                _ovectordouble(c_coord, c_coord_n.value),
                _ovectordouble(c_coordMaster, c_coordMaster_n.value),
            )

        @staticmethod
        def importStl() -> None:
            """gmsh.model.mesh.importStl()

            Import the model STL representation (if available) as the current mesh.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshImportStl(ctypes.byref(ierr))

        @staticmethod
        def getDuplicateNodes(
            dimTags: Sequence[tuple[int, int]] = (),
        ) -> list[int]:
            """gmsh.model.mesh.getDuplicateNodes(dimTags=[])

            Get the `tags` of any duplicate nodes in the mesh of the entities
            `dimTags`, given as a vector of (dim, tag) pairs. If `dimTags` is empty,
            consider the whole mesh.

            Return `tags`.

            Types:
            - `tags`: vector of sizes
            - `dimTags`: vector of pairs of integers
            """
            c_tags, c_tags_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetDuplicateNodes(
                    ctypes.byref(c_tags),
                    ctypes.byref(c_tags_n),
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_tags, c_tags_n.value)

        @staticmethod
        def removeDuplicateNodes(
            dimTags: Sequence[tuple[int, int]] = (),
        ) -> None:
            """gmsh.model.mesh.removeDuplicateNodes(dimTags=[])

            Remove duplicate nodes in the mesh of the entities `dimTags`, given as a
            vector of (dim, tag) pairs. If `dimTags` is empty, consider the whole mesh.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRemoveDuplicateNodes(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def removeDuplicateElements(
            dimTags: Sequence[tuple[int, int]] = (),
        ) -> None:
            """gmsh.model.mesh.removeDuplicateElements(dimTags=[])

            Remove duplicate elements (defined by the same nodes, in the same entity)
            in the mesh of the entities `dimTags`, given as a vector of (dim, tag)
            pairs. If `dimTags` is empty, consider the whole mesh.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshRemoveDuplicateElements(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def splitQuadrangles(*, quality: float = 1.0, tag: int = -1) -> None:
            """gmsh.model.mesh.splitQuadrangles(quality=1., tag=-1)

            Split (into two triangles) all quadrangles in surface `tag` whose quality
            is lower than `quality`. If `tag` < 0, split quadrangles in all surfaces.

            Types:
            - `quality`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSplitQuadrangles(
                    ctypes.c_double(quality),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def setVisibility(elementTags: Sequence[int], value: int) -> None:
            """gmsh.model.mesh.setVisibility(elementTags, value)

            Set the visibility of the elements of tags `elementTags` to `value`.

            Types:
            - `elementTags`: vector of sizes
            - `value`: integer
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshSetVisibility(
                    c_elementTags,
                    c_elementTags_n,
                    ctypes.c_int(value),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getVisibility(elementTags: Sequence[int]) -> list[int]:
            """gmsh.model.mesh.getVisibility(elementTags)

            Get the visibility of the elements of tags `elementTags`.

            Return `values`.

            Types:
            - `elementTags`: vector of sizes
            - `values`: vector of integers
            """
            c_elementTags, c_elementTags_n = _ivectorsize(elementTags)
            c_values = ctypes.POINTER(ctypes.c_int)()
            c_values_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshGetVisibility(
                    c_elementTags,
                    c_elementTags_n,
                    ctypes.byref(c_values),
                    ctypes.byref(c_values_n),
                    ctypes.byref(ierr),
                )

            return _ovectorint(c_values, c_values_n.value)

        @staticmethod
        def classifySurfaces(
            angle: float,
            *,
            boundary: bool = True,
            forReparametrization: bool = False,
            curveAngle: float = math.pi,
            exportDiscrete: bool = True,
        ) -> None:
            """gmsh.model.mesh.classifySurfaces(angle, boundary=True, forReparametrization=False, curveAngle=pi, exportDiscrete=True)

            Classify ("color") the surface mesh based on the angle threshold `angle`
            (in radians), and create new discrete surfaces, curves and points
            accordingly. If `boundary` is set, also create discrete curves on the
            boundary if the surface is open. If `forReparametrization` is set, create
            curves and surfaces that can be reparametrized using a single map. If
            `curveAngle` is less than Pi, also force curves to be split according to
            `curveAngle`. If `exportDiscrete` is set, clear any built-in CAD kernel
            entities and export the discrete entities in the built-in CAD kernel.

            Types:
            - `angle`: double
            - `boundary`: boolean
            - `forReparametrization`: boolean
            - `curveAngle`: double
            - `exportDiscrete`: boolean
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshClassifySurfaces(
                    ctypes.c_double(angle),
                    ctypes.c_int(bool(boundary)),
                    ctypes.c_int(bool(forReparametrization)),
                    ctypes.c_double(curveAngle),
                    ctypes.c_int(bool(exportDiscrete)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def createGeometry(dimTags: Sequence[tuple[int, int]] = ()) -> None:
            """gmsh.model.mesh.createGeometry(dimTags=[])

            Create a geometry for the discrete entities `dimTags` (given as a vector of
            (dim, tag) pairs) represented solely by a mesh (without an underlying CAD
            description), i.e. create a parametrization for discrete curves and
            surfaces, assuming that each can be parametrized with a single map. If
            `dimTags` is empty, create a geometry for all the discrete entities.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshCreateGeometry(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def createTopology(
            *, makeSimplyConnected: bool = True, exportDiscrete: bool = True
        ) -> None:
            """gmsh.model.mesh.createTopology(makeSimplyConnected=True, exportDiscrete=True)

            Create a boundary representation from the mesh if the model does not have
            one (e.g. when imported from mesh file formats with no BRep representation
            of the underlying model). If `makeSimplyConnected` is set, enforce simply
            connected discrete surfaces and volumes. If `exportDiscrete` is set, clear
            any built-in CAD kernel entities and export the discrete entities in the
            built-in CAD kernel.

            Types:
            - `makeSimplyConnected`: boolean
            - `exportDiscrete`: boolean
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshCreateTopology(
                    ctypes.c_int(bool(makeSimplyConnected)),
                    ctypes.c_int(bool(exportDiscrete)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addHomologyRequest(
            *,
            type: str = "Homology",  # noqa: A002
            domainTags: Sequence[int] = (),
            subdomainTags: Sequence[int] = (),
            dims: Sequence[int] = (),
        ) -> None:
            """gmsh.model.mesh.addHomologyRequest(type="Homology", domainTags=[], subdomainTags=[], dims=[])

            Add a request to compute a basis representation for homology spaces (if
            `type` == "Homology") or cohomology spaces (if `type` == "Cohomology"). The
            computation domain is given in a list of physical group tags `domainTags`;
            if empty, the whole mesh is the domain. The computation subdomain for
            relative (co)homology computation is given in a list of physical group tags
            `subdomainTags`; if empty, absolute (co)homology is computed. The
            dimensions of the (co)homology bases to be computed are given in the list
            `dim`; if empty, all bases are computed. Resulting basis representation
            (co)chains are stored as physical groups in the mesh. If the request is
            added before mesh generation, the computation will be performed at the end
            of the meshing pipeline.

            Types:
            - `type`: string
            - `domainTags`: vector of integers
            - `subdomainTags`: vector of integers
            - `dims`: vector of integers
            """
            c_domainTags, c_domainTags_n = _ivectorint(domainTags)
            c_subdomainTags, c_subdomainTags_n = _ivectorint(subdomainTags)
            c_dims, c_dims_n = _ivectorint(dims)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshAddHomologyRequest(
                    ctypes.c_char_p(type.encode()),
                    c_domainTags,
                    c_domainTags_n,
                    c_subdomainTags,
                    c_subdomainTags_n,
                    c_dims,
                    c_dims_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def clearHomologyRequests() -> None:
            """gmsh.model.mesh.clearHomologyRequests()

            Clear all (co)homology computation requests.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshClearHomologyRequests(ctypes.byref(ierr))

        @staticmethod
        def computeHomology() -> list[tuple[int, int]]:
            """gmsh.model.mesh.computeHomology()

            Perform the (co)homology computations requested by addHomologyRequest().
            The newly created physical groups are returned in `dimTags` as a vector of
            (dim, tag) pairs.

            Return `dimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags = ctypes.POINTER(ctypes.c_int)()
            c_dimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshComputeHomology(
                    ctypes.byref(c_dimTags),
                    ctypes.byref(c_dimTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_dimTags, c_dimTags_n.value)

        @staticmethod
        def computeCrossField() -> list[int]:
            """gmsh.model.mesh.computeCrossField()

            Compute a cross field for the current mesh. The function creates 3 views:
            the H function, the Theta function and cross directions. Return the tags of
            the views.

            Return `viewTags`.

            Types:
            - `viewTags`: vector of integers
            """
            c_viewTags = ctypes.POINTER(ctypes.c_int)()
            c_viewTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshComputeCrossField(
                    ctypes.byref(c_viewTags),
                    ctypes.byref(c_viewTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorint(c_viewTags, c_viewTags_n.value)

        @staticmethod
        def triangulate(coord: Sequence[float]) -> list[int]:
            """gmsh.model.mesh.triangulate(coord)

            Triangulate the points given in the `coord` vector as pairs of u, v
            coordinates, and return the node tags (with numbering starting at 1) of the
            resulting triangles in `tri`.

            Return `tri`.

            Types:
            - `coord`: vector of doubles
            - `tri`: vector of sizes
            """
            c_coord, c_coord_n = _ivectordouble(coord)
            c_tri, c_tri_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshTriangulate(
                    c_coord,
                    c_coord_n,
                    ctypes.byref(c_tri),
                    ctypes.byref(c_tri_n),
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_tri, c_tri_n.value)

        @staticmethod
        def tetrahedralize(coord: Sequence[float]) -> list[int]:
            """gmsh.model.mesh.tetrahedralize(coord)

            Tetrahedralize the points given in the `coord` vector as x, y, z
            coordinates, concatenated, and return the node tags (with numbering
            starting at 1) of the resulting tetrahedra in `tetra`.

            Return `tetra`.

            Types:
            - `coord`: vector of doubles
            - `tetra`: vector of sizes
            """
            c_coord, c_coord_n = _ivectordouble(coord)
            c_tetra, c_tetra_n = (
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelMeshTetrahedralize(
                    c_coord,
                    c_coord_n,
                    ctypes.byref(c_tetra),
                    ctypes.byref(c_tetra_n),
                    ctypes.byref(ierr),
                )

            return _ovectorsize(c_tetra, c_tetra_n.value)

        class field:
            """Mesh size field functions"""

            @staticmethod
            def add(fieldType: str, *, tag: int = -1) -> int:
                """gmsh.model.mesh.field.add(fieldType, tag=-1)

                Add a new mesh size field of type `fieldType`. If `tag` is positive, assign
                the tag explicitly; otherwise a new tag is assigned automatically. Return
                the field tag. Available field types are listed in the "Gmsh mesh size
                fields" chapter of the Gmsh reference manual
                (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-mesh-size-fields).

                Types:
                - `fieldType`: string
                - `tag`: integer
                """
                with _ErrorCode() as ierr:
                    return gmsh.lib.gmshModelMeshFieldAdd(
                        ctypes.c_char_p(fieldType.encode()),
                        ctypes.c_int(tag),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def remove(tag: int) -> None:
                """gmsh.model.mesh.field.remove(tag)

                Remove the field with tag `tag`.

                Types:
                - `tag`: integer
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldRemove(
                        ctypes.c_int(tag), ctypes.byref(ierr)
                    )

            @staticmethod
            def list() -> list[int]:
                """gmsh.model.mesh.field.list()

                Get the list of all fields.

                Return `tags`.

                Types:
                - `tags`: vector of integers
                """
                c_tags = ctypes.POINTER(ctypes.c_int)()
                c_tags_n = ctypes.c_size_t()
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldList(
                        ctypes.byref(c_tags),
                        ctypes.byref(c_tags_n),
                        ctypes.byref(ierr),
                    )

                return _ovectorint(c_tags, c_tags_n.value)

            @staticmethod
            def getType(tag: int) -> str:
                """gmsh.model.mesh.field.getType(tag)

                Get the type `fieldType` of the field with tag `tag`.

                Return `fileType`.

                Types:
                - `tag`: integer
                - `fileType`: string
                """
                c_fileType = ctypes.c_char_p()
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldGetType(
                        ctypes.c_int(tag),
                        ctypes.byref(c_fileType),
                        ctypes.byref(ierr),
                    )

                return _ostring(c_fileType)

            @staticmethod
            def setNumber(tag: int, option: str, value: float) -> None:
                """gmsh.model.mesh.field.setNumber(tag, option, value)

                Set the numerical option `option` to value `value` for field `tag`.

                Types:
                - `tag`: integer
                - `option`: string
                - `value`: double
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldSetNumber(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(option.encode()),
                        ctypes.c_double(value),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def getNumber(tag: int, option: str) -> float:
                """gmsh.model.mesh.field.getNumber(tag, option)

                Get the value of the numerical option `option` for field `tag`.

                Return `value`.

                Types:
                - `tag`: integer
                - `option`: string
                - `value`: double
                """
                c_value = ctypes.c_double()
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldGetNumber(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(option.encode()),
                        ctypes.byref(c_value),
                        ctypes.byref(ierr),
                    )

                return c_value.value

            @staticmethod
            def setString(tag: int, option: str, value: str) -> None:
                """gmsh.model.mesh.field.setString(tag, option, value)

                Set the string option `option` to value `value` for field `tag`.

                Types:
                - `tag`: integer
                - `option`: string
                - `value`: string
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldSetString(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(option.encode()),
                        ctypes.c_char_p(value.encode()),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def getString(tag: int, option: str) -> str:
                """gmsh.model.mesh.field.getString(tag, option)

                Get the value of the string option `option` for field `tag`.

                Return `value`.

                Types:
                - `tag`: integer
                - `option`: string
                - `value`: string
                """
                c_value = ctypes.c_char_p()
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldGetString(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(option.encode()),
                        ctypes.byref(c_value),
                        ctypes.byref(ierr),
                    )

                return _ostring(c_value)

            @staticmethod
            def setNumbers(
                tag: int, option: str, values: Sequence[float]
            ) -> None:
                """gmsh.model.mesh.field.setNumbers(tag, option, values)

                Set the numerical list option `option` to value `values` for field `tag`.

                Types:
                - `tag`: integer
                - `option`: string
                - `values`: vector of doubles
                """
                c_values, c_values_n = _ivectordouble(values)
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldSetNumbers(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(option.encode()),
                        c_values,
                        c_values_n,
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def getNumbers(tag: int, option: str) -> builtins.list[float]:
                """gmsh.model.mesh.field.getNumbers(tag, option)

                Get the value of the numerical list option `option` for field `tag`.

                Return `values`.

                Types:
                - `tag`: integer
                - `option`: string
                - `values`: vector of doubles
                """
                c_values = ctypes.POINTER(ctypes.c_double)()
                c_values_n = ctypes.c_size_t()
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldGetNumbers(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(option.encode()),
                        ctypes.byref(c_values),
                        ctypes.byref(c_values_n),
                        ctypes.byref(ierr),
                    )

                return _ovectordouble(c_values, c_values_n.value)

            @staticmethod
            def setAsBackgroundMesh(tag: int) -> None:
                """gmsh.model.mesh.field.setAsBackgroundMesh(tag)

                Set the field `tag` as the background mesh size field.

                Types:
                - `tag`: integer
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldSetAsBackgroundMesh(
                        ctypes.c_int(tag), ctypes.byref(ierr)
                    )

            @staticmethod
            def setAsBoundaryLayer(tag: int) -> None:
                """gmsh.model.mesh.field.setAsBoundaryLayer(tag)

                Set the field `tag` as a boundary layer size field.

                Types:
                - `tag`: integer
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelMeshFieldSetAsBoundaryLayer(
                        ctypes.c_int(tag), ctypes.byref(ierr)
                    )

    class geo:
        """Built-in CAD kernel functions"""

        @staticmethod
        def addPoint(
            x: float,
            y: float,
            z: float,
            *,
            meshSize: float = 0.0,
            tag: int = -1,
        ) -> int:
            """gmsh.model.geo.addPoint(x, y, z, meshSize=0., tag=-1)

            Add a geometrical point in the built-in CAD representation, at coordinates
            (`x`, `y`, `z`). If `meshSize` is > 0, add a meshing constraint at that
            point. If `tag` is positive, set the tag explicitly; otherwise a new tag is
            selected automatically. Return the tag of the point. (Note that the point
            will be added in the current model only after `synchronize` is called. This
            behavior holds for all the entities added in the geo module.)

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `meshSize`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddPoint(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(meshSize),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addLine(startTag: int, endTag: int, *, tag: int = -1) -> int:
            """gmsh.model.geo.addLine(startTag, endTag, tag=-1)

            Add a straight line segment in the built-in CAD representation, between the
            two points with tags `startTag` and `endTag`. If `tag` is positive, set the
            tag explicitly; otherwise a new tag is selected automatically. Return the
            tag of the line.

            Types:
            - `startTag`: integer
            - `endTag`: integer
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddLine(
                    ctypes.c_int(startTag),
                    ctypes.c_int(endTag),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCircleArc(
            startTag: int,
            centerTag: int,
            endTag: int,
            *,
            tag: int = -1,
            nx: float = 0.0,
            ny: float = 0.0,
            nz: float = 0.0,
        ) -> int:
            """gmsh.model.geo.addCircleArc(startTag, centerTag, endTag, tag=-1, nx=0., ny=0., nz=0.)

            Add a circle arc (strictly smaller than Pi) in the built-in CAD
            representation, between the two points with tags `startTag` and `endTag`,
            and with center `centerTag`. If `tag` is positive, set the tag explicitly;
            otherwise a new tag is selected automatically. If (`nx`, `ny`, `nz`) != (0,
            0, 0), explicitly set the plane of the circle arc. Return the tag of the
            circle arc.

            Types:
            - `startTag`: integer
            - `centerTag`: integer
            - `endTag`: integer
            - `tag`: integer
            - `nx`: double
            - `ny`: double
            - `nz`: double
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddCircleArc(
                    ctypes.c_int(startTag),
                    ctypes.c_int(centerTag),
                    ctypes.c_int(endTag),
                    ctypes.c_int(tag),
                    ctypes.c_double(nx),
                    ctypes.c_double(ny),
                    ctypes.c_double(nz),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addEllipseArc(
            startTag: int,
            centerTag: int,
            majorTag: int,
            endTag: int,
            *,
            tag: int = -1,
            nx: float = 0.0,
            ny: float = 0.0,
            nz: float = 0.0,
        ) -> int:
            """gmsh.model.geo.addEllipseArc(startTag, centerTag, majorTag, endTag, tag=-1, nx=0., ny=0., nz=0.)

            Add an ellipse arc (strictly smaller than Pi) in the built-in CAD
            representation, between the two points `startTag` and `endTag`, and with
            center `centerTag` and major axis point `majorTag`. If `tag` is positive,
            set the tag explicitly; otherwise a new tag is selected automatically. If
            (`nx`, `ny`, `nz`) != (0, 0, 0), explicitly set the plane of the circle
            arc. Return the tag of the ellipse arc.

            Types:
            - `startTag`: integer
            - `centerTag`: integer
            - `majorTag`: integer
            - `endTag`: integer
            - `tag`: integer
            - `nx`: double
            - `ny`: double
            - `nz`: double
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddEllipseArc(
                    ctypes.c_int(startTag),
                    ctypes.c_int(centerTag),
                    ctypes.c_int(majorTag),
                    ctypes.c_int(endTag),
                    ctypes.c_int(tag),
                    ctypes.c_double(nx),
                    ctypes.c_double(ny),
                    ctypes.c_double(nz),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSpline(pointTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.geo.addSpline(pointTags, tag=-1)

            Add a spline (Catmull-Rom) curve in the built-in CAD representation, going
            through the points `pointTags`. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. Create a
            periodic curve if the first and last points are the same. Return the tag of
            the spline curve.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddSpline(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBSpline(pointTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.geo.addBSpline(pointTags, tag=-1)

            Add a cubic b-spline curve in the built-in CAD representation, with
            `pointTags` control points. If `tag` is positive, set the tag explicitly;
            otherwise a new tag is selected automatically. Creates a periodic curve if
            the first and last points are the same. Return the tag of the b-spline
            curve.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddBSpline(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBezier(pointTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.geo.addBezier(pointTags, tag=-1)

            Add a Bezier curve in the built-in CAD representation, with `pointTags`
            control points. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically.  Return the tag of the Bezier curve.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddBezier(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addPolyline(pointTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.geo.addPolyline(pointTags, tag=-1)

            Add a polyline curve in the built-in CAD representation, going through the
            points `pointTags`. If `tag` is positive, set the tag explicitly; otherwise
            a new tag is selected automatically. Create a periodic curve if the first
            and last points are the same. Return the tag of the polyline curve.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddPolyline(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCompoundSpline(
            curveTags: Sequence[int], *, numIntervals: int = 5, tag: int = -1
        ) -> int:
            """gmsh.model.geo.addCompoundSpline(curveTags, numIntervals=5, tag=-1)

            Add a spline (Catmull-Rom) curve in the built-in CAD representation, going
            through points sampling the curves in `curveTags`. The density of sampling
            points on each curve is governed by `numIntervals`. If `tag` is positive,
            set the tag explicitly; otherwise a new tag is selected automatically.
            Return the tag of the spline.

            Types:
            - `curveTags`: vector of integers
            - `numIntervals`: integer
            - `tag`: integer
            """
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddCompoundSpline(
                    c_curveTags,
                    c_curveTags_n,
                    ctypes.c_int(numIntervals),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCompoundBSpline(
            curveTags: Sequence[int], *, numIntervals: int = 20, tag: int = -1
        ) -> int:
            """gmsh.model.geo.addCompoundBSpline(curveTags, numIntervals=20, tag=-1)

            Add a b-spline curve in the built-in CAD representation, with control
            points sampling the curves in `curveTags`. The density of sampling points
            on each curve is governed by `numIntervals`. If `tag` is positive, set the
            tag explicitly; otherwise a new tag is selected automatically. Return the
            tag of the b-spline.

            Types:
            - `curveTags`: vector of integers
            - `numIntervals`: integer
            - `tag`: integer
            """
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddCompoundBSpline(
                    c_curveTags,
                    c_curveTags_n,
                    ctypes.c_int(numIntervals),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCurveLoop(
            curveTags: Sequence[int], *, tag: int = -1, reorient: bool = False
        ) -> int:
            """gmsh.model.geo.addCurveLoop(curveTags, tag=-1, reorient=False)

            Add a curve loop (a closed wire) in the built-in CAD representation, formed
            by the curves `curveTags`. `curveTags` should contain (signed) tags of
            model entities of dimension 1 forming a closed loop: a negative tag
            signifies that the underlying curve is considered with reversed
            orientation. If `tag` is positive, set the tag explicitly; otherwise a new
            tag is selected automatically. If `reorient` is set, automatically reorient
            the curves if necessary. Return the tag of the curve loop.

            Types:
            - `curveTags`: vector of integers
            - `tag`: integer
            - `reorient`: boolean
            """
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddCurveLoop(
                    c_curveTags,
                    c_curveTags_n,
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(reorient)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCurveLoops(curveTags: Sequence[int]) -> list[int]:
            """gmsh.model.geo.addCurveLoops(curveTags)

            Add curve loops in the built-in CAD representation based on the curves
            `curveTags`. Return the `tags` of found curve loops, if any.

            Return `tags`.

            Types:
            - `curveTags`: vector of integers
            - `tags`: vector of integers
            """
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            c_tags = ctypes.POINTER(ctypes.c_int)()
            c_tags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoAddCurveLoops(
                    c_curveTags,
                    c_curveTags_n,
                    ctypes.byref(c_tags),
                    ctypes.byref(c_tags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorint(c_tags, c_tags_n.value)

        @staticmethod
        def addPlaneSurface(wireTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.geo.addPlaneSurface(wireTags, tag=-1)

            Add a plane surface in the built-in CAD representation, defined by one or
            more curve loops `wireTags`. The first curve loop defines the exterior
            contour; additional curve loop define holes. If `tag` is positive, set the
            tag explicitly; otherwise a new tag is selected automatically. Return the
            tag of the surface.

            Types:
            - `wireTags`: vector of integers
            - `tag`: integer
            """
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddPlaneSurface(
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSurfaceFilling(
            wireTags: Sequence[int],
            *,
            tag: int = -1,
            sphereCenterTag: int = -1,
        ) -> int:
            """gmsh.model.geo.addSurfaceFilling(wireTags, tag=-1, sphereCenterTag=-1)

            Add a surface in the built-in CAD representation, filling the curve loops
            in `wireTags` using transfinite interpolation. Currently only a single
            curve loop is supported; this curve loop should be composed by 3 or 4
            curves only. If `tag` is positive, set the tag explicitly; otherwise a new
            tag is selected automatically. Return the tag of the surface.

            Types:
            - `wireTags`: vector of integers
            - `tag`: integer
            - `sphereCenterTag`: integer
            """
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddSurfaceFilling(
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.c_int(tag),
                    ctypes.c_int(sphereCenterTag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSurfaceLoop(
            surfaceTags: Sequence[int], *, tag: int = -1
        ) -> int:
            """Return the tag of a new surface loop from the given tags.

            Add a surface loop (a closed shell) formed by `surfaceTags` in the
            built-in CAD representation. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically.
            """
            c_surfaceTags, c_surfaceTags_n = _ivectorint(surfaceTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddSurfaceLoop(
                    c_surfaceTags,
                    c_surfaceTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addVolume(shellTags: Sequence[int], *, tag: int = -1) -> int:
            """Return the tag of a new volume defined by one or more shells.

            Add a volume (a region) in the built-in CAD representation, defined
            by one or more shells `shellTags`. The first surface loop defines
            the exterior boundary; additional surface loop define holes. If
            `tag` is positive, set the tag explicitly; otherwise a new tag is
            selected automatically.
            """
            c_shellTags, c_shellTags_n = _ivectorint(shellTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddVolume(
                    c_shellTags,
                    c_shellTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addGeometry(
            geometry: str,
            numbers: Sequence[float] = (),
            strings: Sequence[str] = (),
            *,
            tag: int = -1,
        ) -> int:
            """gmsh.model.geo.addGeometry(geometry, numbers=[], strings=[], tag=-1)

            Add a `geometry` in the built-in CAD representation. `geometry` can
            currently be one of "Sphere" or "PolarSphere" (where `numbers` should
            contain the x, y, z coordinates of the center, followed by the radius), or
            "Parametric" (where `strings` should contains three expression evaluating
            to the x, y and z coordinates. If `tag` is positive, set the tag of the
            geometry explicitly; otherwise a new tag is selected automatically. Return
            the tag of the geometry.

            Types:
            - `geometry`: string
            - `numbers`: vector of doubles
            - `strings`: vector of strings
            - `tag`: integer
            """
            c_numbers, c_numbers_n = _ivectordouble(numbers)
            c_strings, c_strings_n = _ivectorstring(strings)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddGeometry(
                    ctypes.c_char_p(geometry.encode()),
                    c_numbers,
                    c_numbers_n,
                    c_strings,
                    c_strings_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addPointOnGeometry(
            geometryTag: int,
            x: float,
            y: float,
            z: float = 0.0,
            *,
            meshSize: float = 0.0,
            tag: int = -1,
        ) -> int:
            """gmsh.model.geo.addPointOnGeometry(geometryTag, x, y, z=0., meshSize=0., tag=-1)

            Add a point in the built-in CAD representation, at coordinates (`x`, `y`,
            `z`) on the geometry `geometryTag`. If `meshSize` is > 0, add a meshing
            constraint at that point. If `tag` is positive, set the tag explicitly;
            otherwise a new tag is selected automatically. Return the tag of the point.
            For surface geometries, only the `x` and `y` coordinates are used.

            Types:
            - `geometryTag`: integer
            - `x`: double
            - `y`: double
            - `z`: double
            - `meshSize`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddPointOnGeometry(
                    ctypes.c_int(geometryTag),
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(meshSize),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def extrude(
            dimTags: Sequence[tuple[int, int]],
            dx: float,
            dy: float,
            dz: float,
            *,
            numElements: Sequence[int] = (),
            heights: Sequence[float] = (),
            recombine: bool = False,
        ) -> list[tuple[int, int]]:
            """gmsh.model.geo.extrude(dimTags, dx, dy, dz, numElements=[], heights=[], recombine=False)

            Extrude the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation, using a translation along (`dx`, `dy`,
            `dz`). Return extruded entities in `outDimTags`. If the `numElements`
            vector is not empty, also extrude the mesh: the entries in `numElements`
            give the number of elements in each layer. If the `height` vector is not
            empty, it provides the (cumulative) height of the different layers,
            normalized to 1. If `recombine` is set, recombine the mesh in the layers.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `outDimTags`: vector of pairs of integers
            - `numElements`: vector of integers
            - `heights`: vector of doubles
            - `recombine`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_numElements, c_numElements_n = _ivectorint(numElements)
            c_heights, c_heights_n = _ivectordouble(heights)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoExtrude(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_numElements,
                    c_numElements_n,
                    c_heights,
                    c_heights_n,
                    ctypes.c_int(bool(recombine)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def revolve(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
            *,
            numElements: Sequence[int] = (),
            heights: Sequence[float] = (),
            recombine: bool = False,
        ) -> list[tuple[int, int]]:
            """gmsh.model.geo.revolve(dimTags, x, y, z, ax, ay, az, angle, numElements=[], heights=[], recombine=False)

            Extrude the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation, using a rotation of `angle` radians around
            the axis of revolution defined by the point (`x`, `y`, `z`) and the
            direction (`ax`, `ay`, `az`). The angle should be strictly smaller than Pi.
            Return extruded entities in `outDimTags`. If the `numElements` vector is
            not empty, also extrude the mesh: the entries in `numElements` give the
            number of elements in each layer. If the `height` vector is not empty, it
            provides the (cumulative) height of the different layers, normalized to 1.
            If `recombine` is set, recombine the mesh in the layers.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `ax`: double
            - `ay`: double
            - `az`: double
            - `angle`: double
            - `outDimTags`: vector of pairs of integers
            - `numElements`: vector of integers
            - `heights`: vector of doubles
            - `recombine`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_numElements, c_numElements_n = _ivectorint(numElements)
            c_heights, c_heights_n = _ivectordouble(heights)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoRevolve(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(ax),
                    ctypes.c_double(ay),
                    ctypes.c_double(az),
                    ctypes.c_double(angle),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_numElements,
                    c_numElements_n,
                    c_heights,
                    c_heights_n,
                    ctypes.c_int(bool(recombine)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def twist(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
            *,
            numElements: Sequence[int] = (),
            heights: Sequence[float] = (),
            recombine: bool = False,
        ) -> list[tuple[int, int]]:
            """gmsh.model.geo.twist(dimTags, x, y, z, dx, dy, dz, ax, ay, az, angle, numElements=[], heights=[], recombine=False)

            Extrude the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation, using a combined translation and rotation
            of `angle` radians, along (`dx`, `dy`, `dz`) and around the axis of
            revolution defined by the point (`x`, `y`, `z`) and the direction (`ax`,
            `ay`, `az`). The angle should be strictly smaller than Pi. Return extruded
            entities in `outDimTags`. If the `numElements` vector is not empty, also
            extrude the mesh: the entries in `numElements` give the number of elements
            in each layer. If the `height` vector is not empty, it provides the
            (cumulative) height of the different layers, normalized to 1. If
            `recombine` is set, recombine the mesh in the layers.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `ax`: double
            - `ay`: double
            - `az`: double
            - `angle`: double
            - `outDimTags`: vector of pairs of integers
            - `numElements`: vector of integers
            - `heights`: vector of doubles
            - `recombine`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_numElements, c_numElements_n = _ivectorint(numElements)
            c_heights, c_heights_n = _ivectordouble(heights)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoTwist(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.c_double(ax),
                    ctypes.c_double(ay),
                    ctypes.c_double(az),
                    ctypes.c_double(angle),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_numElements,
                    c_numElements_n,
                    c_heights,
                    c_heights_n,
                    ctypes.c_int(bool(recombine)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def extrudeBoundaryLayer(
            dimTags: Sequence[tuple[int, int]],
            numElements: Sequence[int] = (1,),
            heights: Sequence[float] = (),
            *,
            recombine: bool = False,
            second: bool = False,
            viewIndex: int = -1,
        ) -> list[tuple[int, int]]:
            """gmsh.model.geo.extrudeBoundaryLayer(dimTags, numElements=[1], heights=[], recombine=False, second=False, viewIndex=-1)

            Extrude the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation along the normals of the mesh, creating
            discrete boundary layer entities. Return extruded entities in `outDimTags`.
            The entries in `numElements` give the number of elements in each layer. If
            the `height` vector is not empty, it provides the (cumulative) height of
            the different layers. If `recombine` is set, recombine the mesh in the
            layers. A second boundary layer can be created from the same entities if
            `second` is set. If `viewIndex` is >= 0, use the corresponding view to
            either specify the normals (if the view contains a vector field) or scale
            the normals (if the view is scalar).

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            - `numElements`: vector of integers
            - `heights`: vector of doubles
            - `recombine`: boolean
            - `second`: boolean
            - `viewIndex`: integer
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_numElements, c_numElements_n = _ivectorint(numElements)
            c_heights, c_heights_n = _ivectordouble(heights)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoExtrudeBoundaryLayer(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_numElements,
                    c_numElements_n,
                    c_heights,
                    c_heights_n,
                    ctypes.c_int(bool(recombine)),
                    ctypes.c_int(bool(second)),
                    ctypes.c_int(viewIndex),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def translate(
            dimTags: Sequence[tuple[int, int]], dx: float, dy: float, dz: float
        ) -> None:
            """gmsh.model.geo.translate(dimTags, dx, dy, dz)

            Translate the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation along (`dx`, `dy`, `dz`).

            Types:
            - `dimTags`: vector of pairs of integers
            - `dx`: double
            - `dy`: double
            - `dz`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoTranslate(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def rotate(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
        ) -> None:
            """gmsh.model.geo.rotate(dimTags, x, y, z, ax, ay, az, angle)

            Rotate the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation by `angle` radians around the axis of
            revolution defined by the point (`x`, `y`, `z`) and the direction (`ax`,
            `ay`, `az`).

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `ax`: double
            - `ay`: double
            - `az`: double
            - `angle`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoRotate(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(ax),
                    ctypes.c_double(ay),
                    ctypes.c_double(az),
                    ctypes.c_double(angle),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def dilate(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            a: float,
            b: float,
            c: float,
        ) -> None:
            """gmsh.model.geo.dilate(dimTags, x, y, z, a, b, c)

            Scale the entities `dimTags` (given as a vector of (dim, tag) pairs) in the
            built-in CAD representation by factors `a`, `b` and `c` along the three
            coordinate axes; use (`x`, `y`, `z`) as the center of the homothetic
            transformation.

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `a`: double
            - `b`: double
            - `c`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoDilate(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(a),
                    ctypes.c_double(b),
                    ctypes.c_double(c),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def mirror(
            dimTags: Sequence[tuple[int, int]],
            a: float,
            b: float,
            c: float,
            d: float,
        ) -> None:
            """gmsh.model.geo.mirror(dimTags, a, b, c, d)

            Mirror the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation, with respect to the plane of equation `a`
            * x + `b` * y + `c` * z + `d` = 0.

            Types:
            - `dimTags`: vector of pairs of integers
            - `a`: double
            - `b`: double
            - `c`: double
            - `d`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoMirror(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(a),
                    ctypes.c_double(b),
                    ctypes.c_double(c),
                    ctypes.c_double(d),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def symmetrize(
            dimTags: Sequence[tuple[int, int]],
            a: float,
            b: float,
            c: float,
            d: float,
        ) -> None:
            """gmsh.model.geo.symmetrize(dimTags, a, b, c, d)

            Mirror the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation, with respect to the plane of equation `a`
            * x + `b` * y + `c` * z + `d` = 0. (This is a synonym for `mirror`, which
            will be deprecated in a future release.)

            Types:
            - `dimTags`: vector of pairs of integers
            - `a`: double
            - `b`: double
            - `c`: double
            - `d`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoSymmetrize(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(a),
                    ctypes.c_double(b),
                    ctypes.c_double(c),
                    ctypes.c_double(d),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def copy(dimTags: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
            """gmsh.model.geo.copy(dimTags)

            Copy the entities `dimTags` (given as a vector of (dim, tag) pairs) in the
            built-in CAD representation; the new entities are returned in `outDimTags`.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoCopy(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def remove(
            dimTags: Sequence[tuple[int, int]], *, recursive: bool = False
        ) -> None:
            """gmsh.model.geo.remove(dimTags, recursive=False)

            Remove the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the built-in CAD representation, provided that they are not on the boundary
            of higher-dimensional entities. If `recursive` is true, remove all the
            entities on their boundaries, down to dimension 0.

            Types:
            - `dimTags`: vector of pairs of integers
            - `recursive`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoRemove(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_int(bool(recursive)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def removeAllDuplicates() -> None:
            """gmsh.model.geo.removeAllDuplicates()

            Remove all duplicate entities in the built-in CAD representation (different
            entities at the same geometrical location).
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoRemoveAllDuplicates(ctypes.byref(ierr))

        @staticmethod
        def splitCurve(tag: int, pointTags: Sequence[int]) -> list[int]:
            """gmsh.model.geo.splitCurve(tag, pointTags)

            Split the curve of tag `tag` in the built-in CAD representation, on the
            specified control points `pointTags`. This feature is only available for
            lines, splines and b-splines. Return the tag(s) `curveTags` of the newly
            created curve(s).

            Return `curveTags`.

            Types:
            - `tag`: integer
            - `pointTags`: vector of integers
            - `curveTags`: vector of integers
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            c_curveTags = ctypes.POINTER(ctypes.c_int)()
            c_curveTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoSplitCurve(
                    ctypes.c_int(tag),
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.byref(c_curveTags),
                    ctypes.byref(c_curveTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorint(c_curveTags, c_curveTags_n.value)

        @staticmethod
        def getMaxTag(dim: int) -> int:
            """gmsh.model.geo.getMaxTag(dim)

            Get the maximum tag of entities of dimension `dim` in the built-in CAD
            representation.

            Types:
            - `dim`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoGetMaxTag(
                    ctypes.c_int(dim), ctypes.byref(ierr)
                )

        @staticmethod
        def setMaxTag(dim: int, maxTag: int) -> None:
            """gmsh.model.geo.setMaxTag(dim, maxTag)

            Set the maximum tag `maxTag` for entities of dimension `dim` in the built-
            in CAD representation.

            Types:
            - `dim`: integer
            - `maxTag`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoSetMaxTag(
                    ctypes.c_int(dim), ctypes.c_int(maxTag), ctypes.byref(ierr)
                )

        @staticmethod
        def addPhysicalGroup(
            dim: int, tags: Sequence[int], *, tag: int = -1, name: str = ""
        ) -> int:
            """gmsh.model.geo.addPhysicalGroup(dim, tags, tag=-1, name="")

            Add a physical group of dimension `dim`, grouping the entities with tags
            `tags` in the built-in CAD representation. Return the tag of the physical
            group, equal to `tag` if `tag` is positive, or a new tag if `tag` < 0. Set
            the name of the physical group if `name` is not empty.

            Types:
            - `dim`: integer
            - `tags`: vector of integers
            - `tag`: integer
            - `name`: string
            """
            c_tags, c_tags_n = _ivectorint(tags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelGeoAddPhysicalGroup(
                    ctypes.c_int(dim),
                    c_tags,
                    c_tags_n,
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def removePhysicalGroups(
            dimTags: Sequence[tuple[int, int]] = (),
        ) -> None:
            """gmsh.model.geo.removePhysicalGroups(dimTags=[])

            Remove the physical groups `dimTags` (given as a vector of (dim, tag)
            pairs) from the built-in CAD representation. If `dimTags` is empty, remove
            all groups.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoRemovePhysicalGroups(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def synchronize() -> None:
            """gmsh.model.geo.synchronize()

            Synchronize the built-in CAD representation with the current Gmsh model.
            This can be called at any time, but since it involves a non trivial amount
            of processing, the number of synchronization points should normally be
            minimized. Without synchronization the entities in the built-in CAD
            representation are not available to any function outside of the built-in
            CAD kernel functions.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelGeoSynchronize(ctypes.byref(ierr))

        class mesh:
            """Built-in CAD kernel meshing constraints"""

            @staticmethod
            def setSize(
                dimTags: Sequence[tuple[int, int]], size: float
            ) -> None:
                """gmsh.model.geo.mesh.setSize(dimTags, size)

                Set a mesh size constraint on the entities `dimTags` (given as a vector of
                (dim, tag) pairs) in the built-in CAD kernel representation. Currently only
                entities of dimension 0 (points) are handled.

                Types:
                - `dimTags`: vector of pairs of integers
                - `size`: double
                """
                c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetSize(
                        c_dimTags,
                        c_dimTags_n,
                        ctypes.c_double(size),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setTransfiniteCurve(
                tag: int,
                nPoints: int,
                *,
                meshType: str = "Progression",
                coef: float = 1.0,
            ) -> None:
                """gmsh.model.geo.mesh.setTransfiniteCurve(tag, nPoints, meshType="Progression", coef=1.)

                Set a transfinite meshing constraint on the curve `tag` in the built-in CAD
                kernel representation, with `numNodes` nodes distributed according to
                `meshType` and `coef`. Currently supported types are "Progression"
                (geometrical progression with power `coef`) and "Bump" (refinement toward
                both extremities of the curve).

                Types:
                - `tag`: integer
                - `nPoints`: integer
                - `meshType`: string
                - `coef`: double
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetTransfiniteCurve(
                        ctypes.c_int(tag),
                        ctypes.c_int(nPoints),
                        ctypes.c_char_p(meshType.encode()),
                        ctypes.c_double(coef),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setTransfiniteSurface(
                tag: int,
                *,
                arrangement: str = "Left",
                cornerTags: Sequence[int] = (),
            ) -> None:
                """gmsh.model.geo.mesh.setTransfiniteSurface(tag, arrangement="Left", cornerTags=[])

                Set a transfinite meshing constraint on the surface `tag` in the built-in
                CAD kernel representation. `arrangement` describes the arrangement of the
                triangles when the surface is not flagged as recombined: currently
                supported values are "Left", "Right", "AlternateLeft" and "AlternateRight".
                `cornerTags` can be used to specify the (3 or 4) corners of the transfinite
                interpolation explicitly; specifying the corners explicitly is mandatory if
                the surface has more that 3 or 4 points on its boundary.

                Types:
                - `tag`: integer
                - `arrangement`: string
                - `cornerTags`: vector of integers
                """
                c_cornerTags, c_cornerTags_n = _ivectorint(cornerTags)
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetTransfiniteSurface(
                        ctypes.c_int(tag),
                        ctypes.c_char_p(arrangement.encode()),
                        c_cornerTags,
                        c_cornerTags_n,
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setTransfiniteVolume(
                tag: int, *, cornerTags: Sequence[int] = ()
            ) -> None:
                """gmsh.model.geo.mesh.setTransfiniteVolume(tag, cornerTags=[])

                Set a transfinite meshing constraint on the surface `tag` in the built-in
                CAD kernel representation. `cornerTags` can be used to specify the (6 or 8)
                corners of the transfinite interpolation explicitly.

                Types:
                - `tag`: integer
                - `cornerTags`: vector of integers
                """
                c_cornerTags, c_cornerTags_n = _ivectorint(cornerTags)
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetTransfiniteVolume(
                        ctypes.c_int(tag),
                        c_cornerTags,
                        c_cornerTags_n,
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setRecombine(dim: int, tag: int, angle: float = 45.0) -> None:
                """gmsh.model.geo.mesh.setRecombine(dim, tag, angle=45.)

                Set a recombination meshing constraint on the entity of dimension `dim` and
                tag `tag` in the built-in CAD kernel representation. Currently only
                entities of dimension 2 (to recombine triangles into quadrangles) are
                supported; `angle` specifies the threshold angle for the simple
                recombination algorithm.

                Types:
                - `dim`: integer
                - `tag`: integer
                - `angle`: double
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetRecombine(
                        ctypes.c_int(dim),
                        ctypes.c_int(tag),
                        ctypes.c_double(angle),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setSmoothing(dim: int, tag: int, val: int) -> None:
                """gmsh.model.geo.mesh.setSmoothing(dim, tag, val)

                Set a smoothing meshing constraint on the entity of dimension `dim` and tag
                `tag` in the built-in CAD kernel representation. `val` iterations of a
                Laplace smoother are applied.

                Types:
                - `dim`: integer
                - `tag`: integer
                - `val`: integer
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetSmoothing(
                        ctypes.c_int(dim),
                        ctypes.c_int(tag),
                        ctypes.c_int(val),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setReverse(dim: int, tag: int, *, val: bool = True) -> None:
                """gmsh.model.geo.mesh.setReverse(dim, tag, val=True)

                Set a reverse meshing constraint on the entity of dimension `dim` and tag
                `tag` in the built-in CAD kernel representation. If `val` is true, the mesh
                orientation will be reversed with respect to the natural mesh orientation
                (i.e. the orientation consistent with the orientation of the geometry). If
                `val` is false, the mesh is left as-is.

                Types:
                - `dim`: integer
                - `tag`: integer
                - `val`: boolean
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetReverse(
                        ctypes.c_int(dim),
                        ctypes.c_int(tag),
                        ctypes.c_int(bool(val)),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setAlgorithm(dim: int, tag: int, val: int) -> None:
                """gmsh.model.geo.mesh.setAlgorithm(dim, tag, val)

                Set the meshing algorithm on the entity of dimension `dim` and tag `tag` in
                the built-in CAD kernel representation. Currently only supported for `dim`
                == 2.

                Types:
                - `dim`: integer
                - `tag`: integer
                - `val`: integer
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetAlgorithm(
                        ctypes.c_int(dim),
                        ctypes.c_int(tag),
                        ctypes.c_int(val),
                        ctypes.byref(ierr),
                    )

            @staticmethod
            def setSizeFromBoundary(dim: int, tag: int, val: int) -> None:
                """gmsh.model.geo.mesh.setSizeFromBoundary(dim, tag, val)

                Force the mesh size to be extended from the boundary, or not, for the
                entity of dimension `dim` and tag `tag` in the built-in CAD kernel
                representation. Currently only supported for `dim` == 2.

                Types:
                - `dim`: integer
                - `tag`: integer
                - `val`: integer
                """
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelGeoMeshSetSizeFromBoundary(
                        ctypes.c_int(dim),
                        ctypes.c_int(tag),
                        ctypes.c_int(val),
                        ctypes.byref(ierr),
                    )

    class occ:
        """OpenCASCADE CAD kernel functions"""

        @staticmethod
        def addPoint(
            x: float,
            y: float,
            z: float,
            *,
            meshSize: float = 0.0,
            tag: int = -1,
        ) -> int:
            """gmsh.model.occ.addPoint(x, y, z, meshSize=0., tag=-1)

            Add a geometrical point in the OpenCASCADE CAD representation, at
            coordinates (`x`, `y`, `z`). If `meshSize` is > 0, add a meshing constraint
            at that point. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. Return the tag of the point. (Note that
            the point will be added in the current model only after `synchronize` is
            called. This behavior holds for all the entities added in the occ module.)

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `meshSize`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddPoint(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(meshSize),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addLine(startTag: int, endTag: int, *, tag: int = -1) -> int:
            """gmsh.model.occ.addLine(startTag, endTag, tag=-1)

            Add a straight line segment in the OpenCASCADE CAD representation, between
            the two points with tags `startTag` and `endTag`. If `tag` is positive, set
            the tag explicitly; otherwise a new tag is selected automatically. Return
            the tag of the line.

            Types:
            - `startTag`: integer
            - `endTag`: integer
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddLine(
                    ctypes.c_int(startTag),
                    ctypes.c_int(endTag),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCircleArc(
            startTag: int,
            middleTag: int,
            endTag: int,
            *,
            tag: int = -1,
            center: bool = True,
        ) -> int:
            """gmsh.model.occ.addCircleArc(startTag, middleTag, endTag, tag=-1, center=True)

            Add a circle arc in the OpenCASCADE CAD representation, between the two
            points with tags `startTag` and `endTag`, with middle point `middleTag`. If
            `center` is true, the middle point is the center of the circle; otherwise
            the circle goes through the middle point. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. Return the tag
            of the circle arc.

            Types:
            - `startTag`: integer
            - `middleTag`: integer
            - `endTag`: integer
            - `tag`: integer
            - `center`: boolean
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddCircleArc(
                    ctypes.c_int(startTag),
                    ctypes.c_int(middleTag),
                    ctypes.c_int(endTag),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(center)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCircle(
            x: float,
            y: float,
            z: float,
            r: float,
            *,
            tag: int = -1,
            angle1: float = 0.0,
            angle2: float = 2 * math.pi,
            zAxis: Sequence[float] = (),
            xAxis: Sequence[float] = (),
        ) -> int:
            """gmsh.model.occ.addCircle(x, y, z, r, tag=-1, angle1=0., angle2=2*pi, zAxis=[], xAxis=[])

            Add a circle of center (`x`, `y`, `z`) and radius `r` in the OpenCASCADE
            CAD representation. If `tag` is positive, set the tag explicitly; otherwise
            a new tag is selected automatically. If `angle1` and `angle2` are
            specified, create a circle arc between the two angles. If a vector `zAxis`
            of size 3 is provided, use it as the normal to the circle plane (z-axis).
            If a vector `xAxis` of size 3 is provided in addition to `zAxis`, use it to
            define the x-axis. Return the tag of the circle.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `r`: double
            - `tag`: integer
            - `angle1`: double
            - `angle2`: double
            - `zAxis`: vector of doubles
            - `xAxis`: vector of doubles
            """
            c_zAxis, c_zAxis_n = _ivectordouble(zAxis)
            c_xAxis, c_xAxis_n = _ivectordouble(xAxis)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddCircle(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(r),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle1),
                    ctypes.c_double(angle2),
                    c_zAxis,
                    c_zAxis_n,
                    c_xAxis,
                    c_xAxis_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addEllipseArc(
            startTag: int,
            centerTag: int,
            majorTag: int,
            endTag: int,
            *,
            tag: int = -1,
        ) -> int:
            """gmsh.model.occ.addEllipseArc(startTag, centerTag, majorTag, endTag, tag=-1)

            Add an ellipse arc in the OpenCASCADE CAD representation, between the two
            points `startTag` and `endTag`, and with center `centerTag` and major axis
            point `majorTag`. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. Return the tag of the ellipse arc. Note
            that OpenCASCADE does not allow creating ellipse arcs with the major radius
            smaller than the minor radius.

            Types:
            - `startTag`: integer
            - `centerTag`: integer
            - `majorTag`: integer
            - `endTag`: integer
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddEllipseArc(
                    ctypes.c_int(startTag),
                    ctypes.c_int(centerTag),
                    ctypes.c_int(majorTag),
                    ctypes.c_int(endTag),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addEllipse(
            x: float,
            y: float,
            z: float,
            r1: float,
            r2: float,
            *,
            tag: int = -1,
            angle1: float = 0.0,
            angle2: float = 2 * math.pi,
            zAxis: tuple[float, float, float] | None = None,
            xAxis: tuple[float, float, float] | None = None,
        ) -> int:
            """gmsh.model.occ.addEllipse(x, y, z, r1, r2, tag=-1, angle1=0., angle2=2*pi, zAxis=[], xAxis=[])

            Add an ellipse of center (`x`, `y`, `z`) and radii `r1` and `r2` (with `r1`
            >= `r2`) along the x- and y-axes, respectively, in the OpenCASCADE CAD
            representation. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. If `angle1` and `angle2` are specified,
            create an ellipse arc between the two angles. If a vector `zAxis` of size 3
            is provided, use it as the normal to the ellipse plane (z-axis). If a
            vector `xAxis` of size 3 is provided in addition to `zAxis`, use it to
            define the x-axis. Return the tag of the ellipse.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `r1`: double
            - `r2`: double
            - `tag`: integer
            - `angle1`: double
            - `angle2`: double
            - `zAxis`: vector of doubles
            - `xAxis`: vector of doubles
            """
            c_zAxis, c_zAxis_n = _ivectordouble(() if zAxis is None else zAxis)
            c_xAxis, c_xAxis_n = _ivectordouble(() if xAxis is None else xAxis)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddEllipse(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(r1),
                    ctypes.c_double(r2),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle1),
                    ctypes.c_double(angle2),
                    c_zAxis,
                    c_zAxis_n,
                    c_xAxis,
                    c_xAxis_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSpline(
            pointTags: Sequence[int],
            *,
            tag: int = -1,
            tangents: Sequence[float] = (),
        ) -> int:
            """gmsh.model.occ.addSpline(pointTags, tag=-1, tangents=[])

            Add a spline (C2 b-spline) curve in the OpenCASCADE CAD representation,
            going through the points `pointTags`. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. Create a
            periodic curve if the first and last points are the same. Return the tag of
            the spline curve. If the `tangents` vector contains 6 entries, use them as
            concatenated x, y, z components of the initial and final tangents of the
            b-spline; if it contains 3 times as many entries as the number of points,
            use them as concatenated x, y, z components of the tangents at each point,
            unless the norm of the tangent is zero.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            - `tangents`: vector of doubles
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            c_tangents, c_tangents_n = _ivectordouble(tangents)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddSpline(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    c_tangents,
                    c_tangents_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBSpline(
            pointTags: Sequence[int],
            *,
            tag: int = -1,
            degree: int = 3,
            weights: Sequence[float] = (),
            knots: Sequence[float] = (),
            multiplicities: Sequence[int] = (),
        ) -> int:
            """gmsh.model.occ.addBSpline(pointTags, tag=-1, degree=3, weights=[], knots=[], multiplicities=[])

            Add a b-spline curve of degree `degree` in the OpenCASCADE CAD
            representation, with `pointTags` control points. If `weights`, `knots` or
            `multiplicities` are not provided, default parameters are computed
            automatically. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. Create a periodic curve if the first and
            last points are the same. Return the tag of the b-spline curve.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            - `degree`: integer
            - `weights`: vector of doubles
            - `knots`: vector of doubles
            - `multiplicities`: vector of integers
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            c_weights, c_weights_n = _ivectordouble(weights)
            c_knots, c_knots_n = _ivectordouble(knots)
            c_multiplicities, c_multiplicities_n = _ivectorint(multiplicities)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBSpline(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    ctypes.c_int(degree),
                    c_weights,
                    c_weights_n,
                    c_knots,
                    c_knots_n,
                    c_multiplicities,
                    c_multiplicities_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBezier(pointTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.occ.addBezier(pointTags, tag=-1)

            Add a Bezier curve in the OpenCASCADE CAD representation, with `pointTags`
            control points. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. Return the tag of the Bezier curve.

            Types:
            - `pointTags`: vector of integers
            - `tag`: integer
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBezier(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addWire(
            curveTags: Sequence[int],
            *,
            tag: int = -1,
            checkClosed: bool = False,
        ) -> int:
            """gmsh.model.occ.addWire(curveTags, tag=-1, checkClosed=False)

            Add a wire (open or closed) in the OpenCASCADE CAD representation, formed
            by the curves `curveTags`. Note that an OpenCASCADE wire can be made of
            curves that share geometrically identical (but topologically different)
            points. If `tag` is positive, set the tag explicitly; otherwise a new tag
            is selected automatically. Return the tag of the wire.

            Types:
            - `curveTags`: vector of integers
            - `tag`: integer
            - `checkClosed`: boolean
            """
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddWire(
                    c_curveTags,
                    c_curveTags_n,
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(checkClosed)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCurveLoop(curveTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.occ.addCurveLoop(curveTags, tag=-1)

            Add a curve loop (a closed wire) in the OpenCASCADE CAD representation,
            formed by the curves `curveTags`. `curveTags` should contain tags of curves
            forming a closed loop. Negative tags can be specified for compatibility
            with the built-in kernel, but are simply ignored: the wire is oriented
            according to the orientation of its first curve. Note that an OpenCASCADE
            curve loop can be made of curves that share geometrically identical (but
            topologically different) points. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. Return the tag
            of the curve loop.

            Types:
            - `curveTags`: vector of integers
            - `tag`: integer
            """
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddCurveLoop(
                    c_curveTags,
                    c_curveTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addRectangle(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            *,
            tag: int = -1,
            roundedRadius: float = 0.0,
        ) -> int:
            """gmsh.model.occ.addRectangle(x, y, z, dx, dy, tag=-1, roundedRadius=0.)

            Add a rectangle in the OpenCASCADE CAD representation, with lower left
            corner at (`x`, `y`, `z`) and upper right corner at (`x` + `dx`, `y` +
            `dy`, `z`). If `tag` is positive, set the tag explicitly; otherwise a new
            tag is selected automatically. Round the corners if `roundedRadius` is
            nonzero. Return the tag of the rectangle.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `dx`: double
            - `dy`: double
            - `tag`: integer
            - `roundedRadius`: double
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddRectangle(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_int(tag),
                    ctypes.c_double(roundedRadius),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addDisk(
            xc: float,
            yc: float,
            zc: float,
            rx: float,
            ry: float,
            *,
            tag: int = -1,
            zAxis: tuple[float, float, float] | None = None,
            xAxis: tuple[float, float, float] | None = None,
        ) -> int:
            """gmsh.model.occ.addDisk(xc, yc, zc, rx, ry, tag=-1, zAxis=[], xAxis=[])

            Add a disk in the OpenCASCADE CAD representation, with center (`xc`, `yc`,
            `zc`) and radius `rx` along the x-axis and `ry` along the y-axis (`rx` >=
            `ry`). If `tag` is positive, set the tag explicitly; otherwise a new tag is
            selected automatically. If a vector `zAxis` of size 3 is provided, use it
            as the normal to the disk (z-axis). If a vector `xAxis` of size 3 is
            provided in addition to `zAxis`, use it to define the x-axis. Return the
            tag of the disk.

            Types:
            - `xc`: double
            - `yc`: double
            - `zc`: double
            - `rx`: double
            - `ry`: double
            - `tag`: integer
            - `zAxis`: vector of doubles
            - `xAxis`: vector of doubles
            """
            c_zAxis, c_zAxis_n = _ivectordouble(() if zAxis is None else zAxis)
            c_xAxis, c_xAxis_n = _ivectordouble(() if xAxis is None else xAxis)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddDisk(
                    ctypes.c_double(xc),
                    ctypes.c_double(yc),
                    ctypes.c_double(zc),
                    ctypes.c_double(rx),
                    ctypes.c_double(ry),
                    ctypes.c_int(tag),
                    c_zAxis,
                    c_zAxis_n,
                    c_xAxis,
                    c_xAxis_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addPlaneSurface(wireTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.occ.addPlaneSurface(wireTags, tag=-1)

            Add a plane surface in the OpenCASCADE CAD representation, defined by one
            or more curve loops (or closed wires) `wireTags`. The first curve loop
            defines the exterior contour; additional curve loop define holes. If `tag`
            is positive, set the tag explicitly; otherwise a new tag is selected
            automatically. Return the tag of the surface.

            Types:
            - `wireTags`: vector of integers
            - `tag`: integer
            """
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddPlaneSurface(
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSurfaceFilling(
            wireTag: int,
            *,
            tag: int = -1,
            pointTags: Sequence[int] = (),
            degree: int = 2,
            numPointsOnCurves: int = 15,
            numIter: int = 2,
            anisotropic: bool = False,
            tol2d: float = 0.00001,
            tol3d: float = 0.0001,
            tolAng: float = 0.01,
            tolCurv: float = 0.1,
            maxDegree: int = 8,
            maxSegments: int = 9,
        ) -> int:
            """gmsh.model.occ.addSurfaceFilling(wireTag, tag=-1, pointTags=[], degree=2, numPointsOnCurves=15, numIter=2, anisotropic=False, tol2d=0.00001, tol3d=0.0001, tolAng=0.01, tolCurv=0.1, maxDegree=8, maxSegments=9)

            Add a surface in the OpenCASCADE CAD representation, filling the curve loop
            `wireTag`. If `tag` is positive, set the tag explicitly; otherwise a new
            tag is selected automatically. Return the tag of the surface. If
            `pointTags` are provided, force the surface to pass through the given
            points. The other optional arguments are `degree` (the degree of the energy
            criterion to minimize for computing the deformation of the surface),
            `numPointsOnCurves` (the average number of points for discretisation of the
            bounding curves), `numIter` (the maximum number of iterations of the
            optimization process), `anisotropic` (improve performance when the ratio of
            the length along the two parametric coordinates of the surface is high),
            `tol2d` (tolerance to the constraints in the parametric plane of the
            surface), `tol3d` (the maximum distance allowed between the support surface
            and the constraints), `tolAng` (the maximum angle allowed between the
            normal of the surface and the constraints), `tolCurv` (the maximum
            difference of curvature allowed between the surface and the constraint),
            `maxDegree` (the highest degree which the polynomial defining the filling
            surface can have) and, `maxSegments` (the largest number of segments which
            the filling surface can have).

            Types:
            - `wireTag`: integer
            - `tag`: integer
            - `pointTags`: vector of integers
            - `degree`: integer
            - `numPointsOnCurves`: integer
            - `numIter`: integer
            - `anisotropic`: boolean
            - `tol2d`: double
            - `tol3d`: double
            - `tolAng`: double
            - `tolCurv`: double
            - `maxDegree`: integer
            - `maxSegments`: integer
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddSurfaceFilling(
                    ctypes.c_int(wireTag),
                    ctypes.c_int(tag),
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(degree),
                    ctypes.c_int(numPointsOnCurves),
                    ctypes.c_int(numIter),
                    ctypes.c_int(bool(anisotropic)),
                    ctypes.c_double(tol2d),
                    ctypes.c_double(tol3d),
                    ctypes.c_double(tolAng),
                    ctypes.c_double(tolCurv),
                    ctypes.c_int(maxDegree),
                    ctypes.c_int(maxSegments),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBSplineFilling(
            wireTag: int,
            *,
            tag: int = -1,
            type: str = "",  # noqa: A002
        ) -> int:
            """gmsh.model.occ.addBSplineFilling(wireTag, tag=-1, type="")

            Add a BSpline surface in the OpenCASCADE CAD representation, filling the
            curve loop `wireTag`. The curve loop should be made of 2, 3 or 4 curves.
            The optional `type` argument specifies the type of filling: "Stretch"
            creates the flattest patch, "Curved" (the default) creates the most rounded
            patch, and "Coons" creates a rounded patch with less depth than "Curved".
            If `tag` is positive, set the tag explicitly; otherwise a new tag is
            selected automatically. Return the tag of the surface.

            Types:
            - `wireTag`: integer
            - `tag`: integer
            - `type`: string
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBSplineFilling(
                    ctypes.c_int(wireTag),
                    ctypes.c_int(tag),
                    ctypes.c_char_p(type.encode()),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBezierFilling(
            wireTag: int,
            *,
            tag: int = -1,
            type: str = "",  # noqa: A002
        ) -> int:
            """gmsh.model.occ.addBezierFilling(wireTag, tag=-1, type="")

            Add a Bezier surface in the OpenCASCADE CAD representation, filling the
            curve loop `wireTag`. The curve loop should be made of 2, 3 or 4 Bezier
            curves. The optional `type` argument specifies the type of filling:
            "Stretch" creates the flattest patch, "Curved" (the default) creates the
            most rounded patch, and "Coons" creates a rounded patch with less depth
            than "Curved". If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. Return the tag of the surface.

            Types:
            - `wireTag`: integer
            - `tag`: integer
            - `type`: string
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBezierFilling(
                    ctypes.c_int(wireTag),
                    ctypes.c_int(tag),
                    ctypes.c_char_p(type.encode()),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBSplineSurface(
            pointTags: Sequence[int],
            numPointsU: int,
            *,
            tag: int = -1,
            degreeU: int = 3,
            degreeV: int = 3,
            weights: Sequence[float] = (),
            knotsU: Sequence[float] = (),
            knotsV: Sequence[float] = (),
            multiplicitiesU: Sequence[int] = (),
            multiplicitiesV: Sequence[int] = (),
            wireTags: Sequence[int] = (),
            wire3D: bool = False,
        ) -> int:
            """gmsh.model.occ.addBSplineSurface(pointTags, numPointsU, tag=-1, degreeU=3, degreeV=3, weights=[], knotsU=[], knotsV=[], multiplicitiesU=[], multiplicitiesV=[], wireTags=[], wire3D=False)

            Add a b-spline surface of degree `degreeU` x `degreeV` in the OpenCASCADE
            CAD representation, with `pointTags` control points given as a single
            vector [Pu1v1, ... Pu`numPointsU`v1, Pu1v2, ...]. If `weights`, `knotsU`,
            `knotsV`, `multiplicitiesU` or `multiplicitiesV` are not provided, default
            parameters are computed automatically. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. If `wireTags` is
            provided, trim the b-spline patch using the provided wires: the first wire
            defines the external contour, the others define holes. If `wire3D` is set,
            consider wire curves as 3D curves and project them on the b-spline surface;
            otherwise consider the wire curves as defined in the parametric space of
            the surface. Return the tag of the b-spline surface.

            Types:
            - `pointTags`: vector of integers
            - `numPointsU`: integer
            - `tag`: integer
            - `degreeU`: integer
            - `degreeV`: integer
            - `weights`: vector of doubles
            - `knotsU`: vector of doubles
            - `knotsV`: vector of doubles
            - `multiplicitiesU`: vector of integers
            - `multiplicitiesV`: vector of integers
            - `wireTags`: vector of integers
            - `wire3D`: boolean
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            c_weights, c_weights_n = _ivectordouble(weights)
            c_knotsU, c_knotsU_n = _ivectordouble(knotsU)
            c_knotsV, c_knotsV_n = _ivectordouble(knotsV)
            c_multiplicitiesU, c_multiplicitiesU_n = _ivectorint(
                multiplicitiesU
            )
            c_multiplicitiesV, c_multiplicitiesV_n = _ivectorint(
                multiplicitiesV
            )
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBSplineSurface(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(numPointsU),
                    ctypes.c_int(tag),
                    ctypes.c_int(degreeU),
                    ctypes.c_int(degreeV),
                    c_weights,
                    c_weights_n,
                    c_knotsU,
                    c_knotsU_n,
                    c_knotsV,
                    c_knotsV_n,
                    c_multiplicitiesU,
                    c_multiplicitiesU_n,
                    c_multiplicitiesV,
                    c_multiplicitiesV_n,
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.c_int(bool(wire3D)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBezierSurface(
            pointTags: Sequence[int],
            numPointsU: int,
            *,
            tag: int = -1,
            wireTags: Sequence[int] = (),
            wire3D: bool = False,
        ) -> int:
            """gmsh.model.occ.addBezierSurface(pointTags, numPointsU, tag=-1, wireTags=[], wire3D=False)

            Add a Bezier surface in the OpenCASCADE CAD representation, with
            `pointTags` control points given as a single vector [Pu1v1, ...
            Pu`numPointsU`v1, Pu1v2, ...]. If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. If `wireTags` is
            provided, trim the Bezier patch using the provided wires: the first wire
            defines the external contour, the others define holes. If `wire3D` is set,
            consider wire curves as 3D curves and project them on the Bezier surface;
            otherwise consider the wire curves as defined in the parametric space of
            the surface. Return the tag of the Bezier surface.

            Types:
            - `pointTags`: vector of integers
            - `numPointsU`: integer
            - `tag`: integer
            - `wireTags`: vector of integers
            - `wire3D`: boolean
            """
            c_pointTags, c_pointTags_n = _ivectorint(pointTags)
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBezierSurface(
                    c_pointTags,
                    c_pointTags_n,
                    ctypes.c_int(numPointsU),
                    ctypes.c_int(tag),
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.c_int(bool(wire3D)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addTrimmedSurface(
            surfaceTag: int,
            *,
            wireTags: Sequence[int] = (),
            wire3D: bool = False,
            tag: int = -1,
        ) -> int:
            """gmsh.model.occ.addTrimmedSurface(surfaceTag, wireTags=[], wire3D=False, tag=-1)

            Trim the surface `surfaceTag` with the wires `wireTags`, replacing any
            existing trimming curves. The first wire defines the external contour, the
            others define holes. If `wire3D` is set, consider wire curves as 3D curves
            and project them on the surface; otherwise consider the wire curves as
            defined in the parametric space of the surface. If `tag` is positive, set
            the tag explicitly; otherwise a new tag is selected automatically. Return
            the tag of the trimmed surface.

            Types:
            - `surfaceTag`: integer
            - `wireTags`: vector of integers
            - `wire3D`: boolean
            - `tag`: integer
            """
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddTrimmedSurface(
                    ctypes.c_int(surfaceTag),
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.c_int(bool(wire3D)),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSurfaceLoop(
            surfaceTags: Sequence[int], *, tag: int = -1, sewing: bool = False
        ) -> int:
            """gmsh.model.occ.addSurfaceLoop(surfaceTags, tag=-1, sewing=False)

            Add a surface loop (a closed shell) in the OpenCASCADE CAD representation,
            formed by `surfaceTags`.  If `tag` is positive, set the tag explicitly;
            otherwise a new tag is selected automatically. Return the tag of the
            surface loop. Setting `sewing` allows one to build a shell made of surfaces
            that share geometrically identical (but topologically different) curves.

            Types:
            - `surfaceTags`: vector of integers
            - `tag`: integer
            - `sewing`: boolean
            """
            c_surfaceTags, c_surfaceTags_n = _ivectorint(surfaceTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddSurfaceLoop(
                    c_surfaceTags,
                    c_surfaceTags_n,
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(sewing)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addVolume(shellTags: Sequence[int], *, tag: int = -1) -> int:
            """gmsh.model.occ.addVolume(shellTags, tag=-1)

            Add a volume (a region) in the OpenCASCADE CAD representation, defined by
            one or more surface loops `shellTags`. The first surface loop defines the
            exterior boundary; additional surface loop define holes. If `tag` is
            positive, set the tag explicitly; otherwise a new tag is selected
            automatically. Return the tag of the volume.

            Types:
            - `shellTags`: vector of integers
            - `tag`: integer
            """
            c_shellTags, c_shellTags_n = _ivectorint(shellTags)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddVolume(
                    c_shellTags,
                    c_shellTags_n,
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addSphere(
            xc: float,
            yc: float,
            zc: float,
            radius: float,
            *,
            tag: int = -1,
            angle1: float = -math.pi / 2,
            angle2: float = math.pi / 2,
            angle3: float = 2 * math.pi,
        ) -> int:
            """gmsh.model.occ.addSphere(xc, yc, zc, radius, tag=-1, angle1=-pi/2, angle2=pi/2, angle3=2*pi)

            Add a sphere of center (`xc`, `yc`, `zc`) and radius `r` in the OpenCASCADE
            CAD representation. The optional `angle1` and `angle2` arguments define the
            polar angle opening (from -Pi/2 to Pi/2). The optional `angle3` argument
            defines the azimuthal opening (from 0 to 2*Pi). If `tag` is positive, set
            the tag explicitly; otherwise a new tag is selected automatically. Return
            the tag of the sphere.

            Types:
            - `xc`: double
            - `yc`: double
            - `zc`: double
            - `radius`: double
            - `tag`: integer
            - `angle1`: double
            - `angle2`: double
            - `angle3`: double
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddSphere(
                    ctypes.c_double(xc),
                    ctypes.c_double(yc),
                    ctypes.c_double(zc),
                    ctypes.c_double(radius),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle1),
                    ctypes.c_double(angle2),
                    ctypes.c_double(angle3),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addBox(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            *,
            tag: int = -1,
        ) -> int:
            """gmsh.model.occ.addBox(x, y, z, dx, dy, dz, tag=-1)

            Add a parallelepipedic box in the OpenCASCADE CAD representation, defined
            by a point (`x`, `y`, `z`) and the extents along the x-, y- and z-axes. If
            `tag` is positive, set the tag explicitly; otherwise a new tag is selected
            automatically. Return the tag of the box.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddBox(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCylinder(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            r: float,
            *,
            tag: int = -1,
            angle: float = 2 * math.pi,
        ) -> int:
            """gmsh.model.occ.addCylinder(x, y, z, dx, dy, dz, r, tag=-1, angle=2*pi)

            Add a cylinder in the OpenCASCADE CAD representation, defined by the center
            (`x`, `y`, `z`) of its first circular face, the 3 components (`dx`, `dy`,
            `dz`) of the vector defining its axis and its radius `r`. The optional
            `angle` argument defines the angular opening (from 0 to 2*Pi). If `tag` is
            positive, set the tag explicitly; otherwise a new tag is selected
            automatically. Return the tag of the cylinder.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `r`: double
            - `tag`: integer
            - `angle`: double
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddCylinder(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.c_double(r),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addCone(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            r1: float,
            r2: float,
            *,
            tag: int = -1,
            angle: float = 2 * math.pi,
        ) -> int:
            """gmsh.model.occ.addCone(x, y, z, dx, dy, dz, r1, r2, tag=-1, angle=2*pi)

            Add a cone in the OpenCASCADE CAD representation, defined by the center
            (`x`, `y`, `z`) of its first circular face, the 3 components of the vector
            (`dx`, `dy`, `dz`) defining its axis and the two radii `r1` and `r2` of the
            faces (these radii can be zero). If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. `angle` defines
            the optional angular opening (from 0 to 2*Pi). Return the tag of the cone.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `r1`: double
            - `r2`: double
            - `tag`: integer
            - `angle`: double
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddCone(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.c_double(r1),
                    ctypes.c_double(r2),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addWedge(
            x: float,
            y: float,
            z: float,
            dx: float,
            dy: float,
            dz: float,
            *,
            tag: int = -1,
            ltx: float = 0.0,
            zAxis: tuple[float, float, float] | None = None,
        ) -> int:
            """gmsh.model.occ.addWedge(x, y, z, dx, dy, dz, tag=-1, ltx=0., zAxis=[])

            Add a right angular wedge in the OpenCASCADE CAD representation, defined by
            the right-angle point (`x`, `y`, `z`) and the 3 extends along the x-, y-
            and z-axes (`dx`, `dy`, `dz`). If `tag` is positive, set the tag
            explicitly; otherwise a new tag is selected automatically. The optional
            argument `ltx` defines the top extent along the x-axis. If a vector `zAxis`
            of size 3 is provided, use it to define the z-axis. Return the tag of the
            wedge.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `tag`: integer
            - `ltx`: double
            - `zAxis`: vector of doubles
            """
            c_zAxis, c_zAxis_n = _ivectordouble(() if zAxis is None else zAxis)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddWedge(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.c_int(tag),
                    ctypes.c_double(ltx),
                    c_zAxis,
                    c_zAxis_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addTorus(
            x: float,
            y: float,
            z: float,
            r1: float,
            r2: float,
            *,
            tag: int = -1,
            angle: float = 2 * math.pi,
            zAxis: tuple[float, float, float] | None = None,
        ) -> int:
            """gmsh.model.occ.addTorus(x, y, z, r1, r2, tag=-1, angle=2*pi, zAxis=[])

            Add a torus in the OpenCASCADE CAD representation, defined by its center
            (`x`, `y`, `z`) and its 2 radii `r` and `r2`. If `tag` is positive, set the
            tag explicitly; otherwise a new tag is selected automatically. The optional
            argument `angle` defines the angular opening (from 0 to 2*Pi). If a vector
            `zAxis` of size 3 is provided, use it to define the z-axis. Return the tag
            of the torus.

            Types:
            - `x`: double
            - `y`: double
            - `z`: double
            - `r1`: double
            - `r2`: double
            - `tag`: integer
            - `angle`: double
            - `zAxis`: vector of doubles
            """
            c_zAxis, c_zAxis_n = _ivectordouble(() if zAxis is None else zAxis)
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccAddTorus(
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(r1),
                    ctypes.c_double(r2),
                    ctypes.c_int(tag),
                    ctypes.c_double(angle),
                    c_zAxis,
                    c_zAxis_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def addThruSections(
            wireTags: Sequence[int],
            *,
            tag: int = -1,
            makeSolid: bool = True,
            makeRuled: bool = False,
            maxDegree: int = -1,
            continuity: str = "",
            parametrization: str = "",
            smoothing: bool = False,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.addThruSections(wireTags, tag=-1, makeSolid=True, makeRuled=False, maxDegree=-1, continuity="", parametrization="", smoothing=False)

            Add a volume (if the optional argument `makeSolid` is set) or surfaces in
            the OpenCASCADE CAD representation, defined through the open or closed
            wires `wireTags`. If `tag` is positive, set the tag explicitly; otherwise a
            new tag is selected automatically. The new entities are returned in
            `outDimTags` as a vector of (dim, tag) pairs. If the optional argument
            `makeRuled` is set, the surfaces created on the boundary are forced to be
            ruled surfaces. If `maxDegree` is positive, set the maximal degree of
            resulting surface. The optional argument `continuity` allows to specify the
            continuity of the resulting shape ("C0", "G1", "C1", "G2", "C2", "C3",
            "CN"). The optional argument `parametrization` sets the parametrization
            type ("ChordLength", "Centripetal", "IsoParametric"). The optional argument
            `smoothing` determines if smoothing is applied.

            Return `outDimTags`.

            Types:
            - `wireTags`: vector of integers
            - `outDimTags`: vector of pairs of integers
            - `tag`: integer
            - `makeSolid`: boolean
            - `makeRuled`: boolean
            - `maxDegree`: integer
            - `continuity`: string
            - `parametrization`: string
            - `smoothing`: boolean
            """
            c_wireTags, c_wireTags_n = _ivectorint(wireTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccAddThruSections(
                    c_wireTags,
                    c_wireTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(makeSolid)),
                    ctypes.c_int(bool(makeRuled)),
                    ctypes.c_int(maxDegree),
                    ctypes.c_char_p(continuity.encode()),
                    ctypes.c_char_p(parametrization.encode()),
                    ctypes.c_int(bool(smoothing)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def addThickSolid(
            volumeTag: int,
            excludeSurfaceTags: Sequence[int],
            offset: float,
            *,
            tag: int = -1,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.addThickSolid(volumeTag, excludeSurfaceTags, offset, tag=-1)

            Add a hollowed volume in the OpenCASCADE CAD representation, built from an
            initial volume `volumeTag` and a set of faces from this volume
            `excludeSurfaceTags`, which are to be removed. The remaining faces of the
            volume become the walls of the hollowed solid, with thickness `offset`. If
            `tag` is positive, set the tag explicitly; otherwise a new tag is selected
            automatically.

            Return `outDimTags`.

            Types:
            - `volumeTag`: integer
            - `excludeSurfaceTags`: vector of integers
            - `offset`: double
            - `outDimTags`: vector of pairs of integers
            - `tag`: integer
            """
            c_excludeSurfaceTags, c_excludeSurfaceTags_n = _ivectorint(
                excludeSurfaceTags
            )
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccAddThickSolid(
                    ctypes.c_int(volumeTag),
                    c_excludeSurfaceTags,
                    c_excludeSurfaceTags_n,
                    ctypes.c_double(offset),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def extrude(
            dimTags: Sequence[tuple[int, int]],
            dx: float,
            dy: float,
            dz: float,
            *,
            numElements: Sequence[int] = (),
            heights: Sequence[float] = (),
            recombine: bool = False,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.extrude(dimTags, dx, dy, dz, numElements=[], heights=[], recombine=False)

            Extrude the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation, using a translation along (`dx`, `dy`,
            `dz`). Return extruded entities in `outDimTags`. If the `numElements`
            vector is not empty, also extrude the mesh: the entries in `numElements`
            give the number of elements in each layer. If the `height` vector is not
            empty, it provides the (cumulative) height of the different layers,
            normalized to 1. If `recombine` is set, recombine the mesh in the layers.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `dx`: double
            - `dy`: double
            - `dz`: double
            - `outDimTags`: vector of pairs of integers
            - `numElements`: vector of integers
            - `heights`: vector of doubles
            - `recombine`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_numElements, c_numElements_n = _ivectorint(numElements)
            c_heights, c_heights_n = _ivectordouble(heights)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccExtrude(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_numElements,
                    c_numElements_n,
                    c_heights,
                    c_heights_n,
                    ctypes.c_int(bool(recombine)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def revolve(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
            *,
            numElements: Sequence[int] = (),
            heights: Sequence[float] = (),
            recombine: bool = False,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.revolve(dimTags, x, y, z, ax, ay, az, angle, numElements=[], heights=[], recombine=False)

            Extrude the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation, using a rotation of `angle` radians
            around the axis of revolution defined by the point (`x`, `y`, `z`) and the
            direction (`ax`, `ay`, `az`). Return extruded entities in `outDimTags`. If
            the `numElements` vector is not empty, also extrude the mesh: the entries
            in `numElements` give the number of elements in each layer. If the `height`
            vector is not empty, it provides the (cumulative) height of the different
            layers, normalized to 1. When the mesh is extruded the angle should be
            strictly smaller than 2*Pi. If `recombine` is set, recombine the mesh in
            the layers.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `ax`: double
            - `ay`: double
            - `az`: double
            - `angle`: double
            - `outDimTags`: vector of pairs of integers
            - `numElements`: vector of integers
            - `heights`: vector of doubles
            - `recombine`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_numElements, c_numElements_n = _ivectorint(numElements)
            c_heights, c_heights_n = _ivectordouble(heights)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccRevolve(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(ax),
                    ctypes.c_double(ay),
                    ctypes.c_double(az),
                    ctypes.c_double(angle),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_numElements,
                    c_numElements_n,
                    c_heights,
                    c_heights_n,
                    ctypes.c_int(bool(recombine)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def addPipe(
            dimTags: Sequence[tuple[int, int]],
            wireTag: int,
            *,
            trihedron: str = "",
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.addPipe(dimTags, wireTag, trihedron="")

            Add a pipe in the OpenCASCADE CAD representation, by extruding the entities
            `dimTags` (given as a vector of (dim, tag) pairs) along the wire `wireTag`.
            The type of sweep can be specified with `trihedron` (possible values:
            "DiscreteTrihedron", "CorrectedFrenet", "Fixed", "Frenet",
            "ConstantNormal", "Darboux", "GuideAC", "GuidePlan", "GuideACWithContact",
            "GuidePlanWithContact"). If `trihedron` is not provided,
            "DiscreteTrihedron" is assumed. Return the pipe in `outDimTags`.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `wireTag`: integer
            - `outDimTags`: vector of pairs of integers
            - `trihedron`: string
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccAddPipe(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_int(wireTag),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_char_p(trihedron.encode()),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def fillet(
            volumeTags: Sequence[int],
            curveTags: Sequence[int],
            radii: Sequence[float],
            *,
            removeVolume: bool = True,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.fillet(volumeTags, curveTags, radii, removeVolume=True)

            Fillet the volumes `volumeTags` on the curves `curveTags` with radii
            `radii`. The `radii` vector can either contain a single radius, as many
            radii as `curveTags`, or twice as many as `curveTags` (in which case
            different radii are provided for the begin and end points of the curves).
            Return the filleted entities in `outDimTags` as a vector of (dim, tag)
            pairs. Remove the original volume if `removeVolume` is set.

            Return `outDimTags`.

            Types:
            - `volumeTags`: vector of integers
            - `curveTags`: vector of integers
            - `radii`: vector of doubles
            - `outDimTags`: vector of pairs of integers
            - `removeVolume`: boolean
            """
            c_volumeTags, c_volumeTags_n = _ivectorint(volumeTags)
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            c_radii, c_radii_n = _ivectordouble(radii)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccFillet(
                    c_volumeTags,
                    c_volumeTags_n,
                    c_curveTags,
                    c_curveTags_n,
                    c_radii,
                    c_radii_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(bool(removeVolume)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def chamfer(
            volumeTags: Sequence[int],
            curveTags: Sequence[int],
            surfaceTags: Sequence[int],
            distances: Sequence[float],
            *,
            removeVolume: bool = True,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.chamfer(volumeTags, curveTags, surfaceTags, distances, removeVolume=True)

            Chamfer the volumes `volumeTags` on the curves `curveTags` with distances
            `distances` measured on surfaces `surfaceTags`. The `distances` vector can
            either contain a single distance, as many distances as `curveTags` and
            `surfaceTags`, or twice as many as `curveTags` and `surfaceTags` (in which
            case the first in each pair is measured on the corresponding surface in
            `surfaceTags`, the other on the other adjacent surface). Return the
            chamfered entities in `outDimTags`. Remove the original volume if
            `removeVolume` is set.

            Return `outDimTags`.

            Types:
            - `volumeTags`: vector of integers
            - `curveTags`: vector of integers
            - `surfaceTags`: vector of integers
            - `distances`: vector of doubles
            - `outDimTags`: vector of pairs of integers
            - `removeVolume`: boolean
            """
            c_volumeTags, c_volumeTags_n = _ivectorint(volumeTags)
            c_curveTags, c_curveTags_n = _ivectorint(curveTags)
            c_surfaceTags, c_surfaceTags_n = _ivectorint(surfaceTags)
            c_distances, c_distances_n = _ivectordouble(distances)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccChamfer(
                    c_volumeTags,
                    c_volumeTags_n,
                    c_curveTags,
                    c_curveTags_n,
                    c_surfaceTags,
                    c_surfaceTags_n,
                    c_distances,
                    c_distances_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(bool(removeVolume)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def defeature(
            volumeTags: Sequence[int],
            surfaceTags: Sequence[int],
            *,
            removeVolume: bool = True,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.defeature(volumeTags, surfaceTags, removeVolume=True)

            Defeature the volumes `volumeTags` by removing the surfaces `surfaceTags`.
            Return the defeatured entities in `outDimTags`. Remove the original volume
            if `removeVolume` is set.

            Return `outDimTags`.

            Types:
            - `volumeTags`: vector of integers
            - `surfaceTags`: vector of integers
            - `outDimTags`: vector of pairs of integers
            - `removeVolume`: boolean
            """
            c_volumeTags, c_volumeTags_n = _ivectorint(volumeTags)
            c_surfaceTags, c_surfaceTags_n = _ivectorint(surfaceTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccDefeature(
                    c_volumeTags,
                    c_volumeTags_n,
                    c_surfaceTags,
                    c_surfaceTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(bool(removeVolume)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def fillet2D(
            edgeTag1: int, edgeTag2: int, radius: float, *, tag: int = -1
        ) -> int:
            """gmsh.model.occ.fillet2D(edgeTag1, edgeTag2, radius, tag=-1)

            Create a fillet edge between edges `edgeTag1` and `edgeTag2` with radius
            `radius`. The modifed edges keep their tag. If `tag` is positive, set the
            tag explicitly; otherwise a new tag is selected automatically.

            Types:
            - `edgeTag1`: integer
            - `edgeTag2`: integer
            - `radius`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccFillet2D(
                    ctypes.c_int(edgeTag1),
                    ctypes.c_int(edgeTag2),
                    ctypes.c_double(radius),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def chamfer2D(
            edgeTag1: int,
            edgeTag2: int,
            distance1: float,
            distance2: float,
            *,
            tag: int = -1,
        ) -> int:
            """gmsh.model.occ.chamfer2D(edgeTag1, edgeTag2, distance1, distance2, tag=-1)

            Create a chamfer edge between edges `edgeTag1` and `edgeTag2` with
            distance1 `distance1` and distance2 `distance2`. The modifed edges keep
            their tag. If `tag` is positive, set the tag explicitly; otherwise a new
            tag is selected automatically.

            Types:
            - `edgeTag1`: integer
            - `edgeTag2`: integer
            - `distance1`: double
            - `distance2`: double
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccChamfer2D(
                    ctypes.c_int(edgeTag1),
                    ctypes.c_int(edgeTag2),
                    ctypes.c_double(distance1),
                    ctypes.c_double(distance2),
                    ctypes.c_int(tag),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def offsetCurve(
            curveLoopTag: int, offset: float
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.offsetCurve(curveLoopTag, offset)

            Create an offset curve based on the curve loop `curveLoopTag` with offset
            `offset`. Return the offset curves in `outDimTags` as a vector of (dim,
            tag) pairs.

            Return `outDimTags`.

            Types:
            - `curveLoopTag`: integer
            - `offset`: double
            - `outDimTags`: vector of pairs of integers
            """
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccOffsetCurve(
                    ctypes.c_int(curveLoopTag),
                    ctypes.c_double(offset),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def getDistance(
            dim1: int, tag1: int, dim2: int, tag2: int
        ) -> tuple[float, float, float, float, float, float, float]:
            """gmsh.model.occ.getDistance(dim1, tag1, dim2, tag2)

            Find the minimal distance between shape with `dim1` and `tag1` and shape
            with `dim2` and `tag2` and the according coordinates. Return the distance
            in `distance` and the coordinate of the points as `x1`, `y1`, `z1` and
            `x2`, `y2`, `z2`.

            Return `distance`, `x1`, `y1`, `z1`, `x2`, `y2`, `z2`.

            Types:
            - `dim1`: integer
            - `tag1`: integer
            - `dim2`: integer
            - `tag2`: integer
            - `distance`: double
            - `x1`: double
            - `y1`: double
            - `z1`: double
            - `x2`: double
            - `y2`: double
            - `z2`: double
            """
            c_distance = ctypes.c_double()
            c_x1 = ctypes.c_double()
            c_y1 = ctypes.c_double()
            c_z1 = ctypes.c_double()
            c_x2 = ctypes.c_double()
            c_y2 = ctypes.c_double()
            c_z2 = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetDistance(
                    ctypes.c_int(dim1),
                    ctypes.c_int(tag1),
                    ctypes.c_int(dim2),
                    ctypes.c_int(tag2),
                    ctypes.byref(c_distance),
                    ctypes.byref(c_x1),
                    ctypes.byref(c_y1),
                    ctypes.byref(c_z1),
                    ctypes.byref(c_x2),
                    ctypes.byref(c_y2),
                    ctypes.byref(c_z2),
                    ctypes.byref(ierr),
                )

            return (
                c_distance.value,
                c_x1.value,
                c_y1.value,
                c_z1.value,
                c_x2.value,
                c_y2.value,
                c_z2.value,
            )

        @staticmethod
        def fuse(
            objectDimTags: Sequence[tuple[int, int]],
            toolDimTags: Sequence[tuple[int, int]],
            *,
            tag: int = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[list[tuple[int, int]], list[list[tuple[int, int]]]]:
            """gmsh.model.occ.fuse(objectDimTags, toolDimTags, tag=-1, removeObject=True, removeTool=True)

            Compute the boolean union (the fusion) of the entities `objectDimTags` and
            `toolDimTags` (vectors of (dim, tag) pairs) in the OpenCASCADE CAD
            representation. Return the resulting entities in `outDimTags`. If `tag` is
            positive, try to set the tag explicitly (only valid if the boolean
            operation results in a single entity). Remove the object if `removeObject`
            is set. Remove the tool if `removeTool` is set.

            Return `outDimTags`, `outDimTagsMap`.

            Types:
            - `objectDimTags`: vector of pairs of integers
            - `toolDimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            - `outDimTagsMap`: vector of vectors of pairs of integers
            - `tag`: integer
            - `removeObject`: boolean
            - `removeTool`: boolean
            """
            c_objectDimTags, c_objectDimTags_n = _ivectorpair(objectDimTags)
            c_toolDimTags, c_toolDimTags_n = _ivectorpair(toolDimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccFuse(
                    c_objectDimTags,
                    c_objectDimTags_n,
                    c_toolDimTags,
                    c_toolDimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(c_outDimTagsMap),
                    ctypes.byref(c_outDimTagsMap_n),
                    ctypes.byref(c_outDimTagsMap_nn),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(removeObject)),
                    ctypes.c_int(bool(removeTool)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorpair(c_outDimTags, c_outDimTags_n.value),
                _ovectorvectorpair(
                    c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn
                ),
            )

        @staticmethod
        def intersect(
            objectDimTags: Sequence[tuple[int, int]],
            toolDimTags: Sequence[tuple[int, int]],
            *,
            tag: int = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[list[tuple[int, int]], list[list[tuple[int, int]]]]:
            """gmsh.model.occ.intersect(objectDimTags, toolDimTags, tag=-1, removeObject=True, removeTool=True)

            Compute the boolean intersection (the common parts) of the entities
            `objectDimTags` and `toolDimTags` (vectors of (dim, tag) pairs) in the
            OpenCASCADE CAD representation. Return the resulting entities in
            `outDimTags`. If `tag` is positive, try to set the tag explicitly (only
            valid if the boolean operation results in a single entity). Remove the
            object if `removeObject` is set. Remove the tool if `removeTool` is set.

            Return `outDimTags`, `outDimTagsMap`.

            Types:
            - `objectDimTags`: vector of pairs of integers
            - `toolDimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            - `outDimTagsMap`: vector of vectors of pairs of integers
            - `tag`: integer
            - `removeObject`: boolean
            - `removeTool`: boolean
            """
            c_objectDimTags, c_objectDimTags_n = _ivectorpair(objectDimTags)
            c_toolDimTags, c_toolDimTags_n = _ivectorpair(toolDimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccIntersect(
                    c_objectDimTags,
                    c_objectDimTags_n,
                    c_toolDimTags,
                    c_toolDimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(c_outDimTagsMap),
                    ctypes.byref(c_outDimTagsMap_n),
                    ctypes.byref(c_outDimTagsMap_nn),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(removeObject)),
                    ctypes.c_int(bool(removeTool)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorpair(c_outDimTags, c_outDimTags_n.value),
                _ovectorvectorpair(
                    c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn
                ),
            )

        @staticmethod
        def cut(
            objectDimTags: Sequence[tuple[int, int]],
            toolDimTags: Sequence[tuple[int, int]],
            *,
            tag: int = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[list[tuple[int, int]], list[list[tuple[int, int]]]]:
            """gmsh.model.occ.cut(objectDimTags, toolDimTags, tag=-1, removeObject=True, removeTool=True)

            Compute the boolean difference between the entities `objectDimTags` and
            `toolDimTags` (given as vectors of (dim, tag) pairs) in the OpenCASCADE CAD
            representation. Return the resulting entities in `outDimTags`. If `tag` is
            positive, try to set the tag explicitly (only valid if the boolean
            operation results in a single entity). Remove the object if `removeObject`
            is set. Remove the tool if `removeTool` is set.

            Return `outDimTags`, `outDimTagsMap`.

            Types:
            - `objectDimTags`: vector of pairs of integers
            - `toolDimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            - `outDimTagsMap`: vector of vectors of pairs of integers
            - `tag`: integer
            - `removeObject`: boolean
            - `removeTool`: boolean
            """
            c_objectDimTags, c_objectDimTags_n = _ivectorpair(objectDimTags)
            c_toolDimTags, c_toolDimTags_n = _ivectorpair(toolDimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccCut(
                    c_objectDimTags,
                    c_objectDimTags_n,
                    c_toolDimTags,
                    c_toolDimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(c_outDimTagsMap),
                    ctypes.byref(c_outDimTagsMap_n),
                    ctypes.byref(c_outDimTagsMap_nn),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(removeObject)),
                    ctypes.c_int(bool(removeTool)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorpair(c_outDimTags, c_outDimTags_n.value),
                _ovectorvectorpair(
                    c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn
                ),
            )

        @staticmethod
        def fragment(
            objectDimTags: Sequence[tuple[int, int]],
            toolDimTags: Sequence[tuple[int, int]],
            *,
            tag: int = -1,
            removeObject: bool = True,
            removeTool: bool = True,
        ) -> tuple[list[tuple[int, int]], list[list[tuple[int, int]]]]:
            """gmsh.model.occ.fragment(objectDimTags, toolDimTags, tag=-1, removeObject=True, removeTool=True)

            Compute the boolean fragments (general fuse) resulting from the
            intersection of the entities `objectDimTags` and `toolDimTags` (given as
            vectors of (dim, tag) pairs) in the OpenCASCADE CAD representation, making
            all interfaces conformal. When applied to entities of different dimensions,
            the lower dimensional entities will be automatically embedded in the higher
            dimensional entities if they are not on their boundary. Return the
            resulting entities in `outDimTags`. If `tag` is positive, try to set the
            tag explicitly (only valid if the boolean operation results in a single
            entity). Remove the object if `removeObject` is set. Remove the tool if
            `removeTool` is set.

            Return `outDimTags`, `outDimTagsMap`.

            Types:
            - `objectDimTags`: vector of pairs of integers
            - `toolDimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            - `outDimTagsMap`: vector of vectors of pairs of integers
            - `tag`: integer
            - `removeObject`: boolean
            - `removeTool`: boolean
            """
            c_objectDimTags, c_objectDimTags_n = _ivectorpair(objectDimTags)
            c_toolDimTags, c_toolDimTags_n = _ivectorpair(toolDimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccFragment(
                    c_objectDimTags,
                    c_objectDimTags_n,
                    c_toolDimTags,
                    c_toolDimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(c_outDimTagsMap),
                    ctypes.byref(c_outDimTagsMap_n),
                    ctypes.byref(c_outDimTagsMap_nn),
                    ctypes.c_int(tag),
                    ctypes.c_int(bool(removeObject)),
                    ctypes.c_int(bool(removeTool)),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorpair(c_outDimTags, c_outDimTags_n.value),
                _ovectorvectorpair(
                    c_outDimTagsMap, c_outDimTagsMap_n, c_outDimTagsMap_nn
                ),
            )

        @staticmethod
        def translate(
            dimTags: Sequence[tuple[int, int]], dx: float, dy: float, dz: float
        ) -> None:
            """gmsh.model.occ.translate(dimTags, dx, dy, dz)

            Translate the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation along (`dx`, `dy`, `dz`).

            Types:
            - `dimTags`: vector of pairs of integers
            - `dx`: double
            - `dy`: double
            - `dz`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccTranslate(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(dx),
                    ctypes.c_double(dy),
                    ctypes.c_double(dz),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def rotate(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            ax: float,
            ay: float,
            az: float,
            angle: float,
        ) -> None:
            """gmsh.model.occ.rotate(dimTags, x, y, z, ax, ay, az, angle)

            Rotate the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation by `angle` radians around the axis of
            revolution defined by the point (`x`, `y`, `z`) and the direction (`ax`,
            `ay`, `az`).

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `ax`: double
            - `ay`: double
            - `az`: double
            - `angle`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccRotate(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(ax),
                    ctypes.c_double(ay),
                    ctypes.c_double(az),
                    ctypes.c_double(angle),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def dilate(
            dimTags: Sequence[tuple[int, int]],
            x: float,
            y: float,
            z: float,
            a: float,
            b: float,
            c: float,
        ) -> None:
            """gmsh.model.occ.dilate(dimTags, x, y, z, a, b, c)

            Scale the entities `dimTags` (given as a vector of (dim, tag) pairs) in the
            OpenCASCADE CAD representation by factors `a`, `b` and `c` along the three
            coordinate axes; use (`x`, `y`, `z`) as the center of the homothetic
            transformation.

            Types:
            - `dimTags`: vector of pairs of integers
            - `x`: double
            - `y`: double
            - `z`: double
            - `a`: double
            - `b`: double
            - `c`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccDilate(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(x),
                    ctypes.c_double(y),
                    ctypes.c_double(z),
                    ctypes.c_double(a),
                    ctypes.c_double(b),
                    ctypes.c_double(c),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def mirror(
            dimTags: Sequence[tuple[int, int]],
            a: float,
            b: float,
            c: float,
            d: float,
        ) -> None:
            """gmsh.model.occ.mirror(dimTags, a, b, c, d)

            Mirror the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation, with respect to the plane of equation
            `a` * x + `b` * y + `c` * z + `d` = 0.

            Types:
            - `dimTags`: vector of pairs of integers
            - `a`: double
            - `b`: double
            - `c`: double
            - `d`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccMirror(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(a),
                    ctypes.c_double(b),
                    ctypes.c_double(c),
                    ctypes.c_double(d),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def symmetrize(
            dimTags: Sequence[tuple[int, int]],
            a: float,
            b: float,
            c: float,
            d: float,
        ) -> None:
            """gmsh.model.occ.symmetrize(dimTags, a, b, c, d)

            Mirror the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation, with respect to the plane of equation
            `a` * x + `b` * y + `c` * z + `d` = 0. (This is a deprecated synonym for
            `mirror`.)

            Types:
            - `dimTags`: vector of pairs of integers
            - `a`: double
            - `b`: double
            - `c`: double
            - `d`: double
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccSymmetrize(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(a),
                    ctypes.c_double(b),
                    ctypes.c_double(c),
                    ctypes.c_double(d),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def affineTransform(
            dimTags: Sequence[tuple[int, int]],
            affineTransform: Sequence[float],
        ) -> None:
            """gmsh.model.occ.affineTransform(dimTags, affineTransform)

            Apply a general affine transformation matrix `affineTransform` (16 entries
            of a 4x4 matrix, by row; only the 12 first can be provided for convenience)
            to the entities `dimTags` (given as a vector of (dim, tag) pairs) in the
            OpenCASCADE CAD representation.

            Types:
            - `dimTags`: vector of pairs of integers
            - `affineTransform`: vector of doubles
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_affineTransform, c_affineTransform_n = _ivectordouble(
                affineTransform
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccAffineTransform(
                    c_dimTags,
                    c_dimTags_n,
                    c_affineTransform,
                    c_affineTransform_n,
                    ctypes.byref(ierr),
                )

        @staticmethod
        def copy(dimTags: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
            """gmsh.model.occ.copy(dimTags)

            Copy the entities `dimTags` in the OpenCASCADE CAD representation; the new
            entities are returned in `outDimTags`.

            Return `outDimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `outDimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccCopy(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def remove(
            dimTags: Sequence[tuple[int, int]], *, recursive: bool = False
        ) -> None:
            """gmsh.model.occ.remove(dimTags, recursive=False)

            Remove the entities `dimTags` (given as a vector of (dim, tag) pairs) in
            the OpenCASCADE CAD representation, provided that they are not on the
            boundary of higher-dimensional entities. If `recursive` is true, remove all
            the entities on their boundaries, down to dimension 0.

            Types:
            - `dimTags`: vector of pairs of integers
            - `recursive`: boolean
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccRemove(
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_int(bool(recursive)),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def removeAllDuplicates() -> None:
            """gmsh.model.occ.removeAllDuplicates()

            Remove all duplicate entities in the OpenCASCADE CAD representation
            (different entities at the same geometrical location) after intersecting
            (using boolean fragments) all highest dimensional entities.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccRemoveAllDuplicates(ctypes.byref(ierr))

        @staticmethod
        def healShapes(
            dimTags: Sequence[tuple[int, int]] = (),
            *,
            tolerance: float = 1e-8,
            fixDegenerated: bool = True,
            fixSmallEdges: bool = True,
            fixSmallFaces: bool = True,
            sewFaces: bool = True,
            makeSolids: bool = True,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.healShapes(dimTags=[], tolerance=1e-8, fixDegenerated=True, fixSmallEdges=True, fixSmallFaces=True, sewFaces=True, makeSolids=True)

            Apply various healing procedures to the entities `dimTags` (given as a
            vector of (dim, tag) pairs), or to all the entities in the model if
            `dimTags` is empty, in the OpenCASCADE CAD representation. Return the
            healed entities in `outDimTags`.

            Return `outDimTags`.

            Types:
            - `outDimTags`: vector of pairs of integers
            - `dimTags`: vector of pairs of integers
            - `tolerance`: double
            - `fixDegenerated`: boolean
            - `fixSmallEdges`: boolean
            - `fixSmallFaces`: boolean
            - `sewFaces`: boolean
            - `makeSolids`: boolean
            """
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccHealShapes(
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    c_dimTags,
                    c_dimTags_n,
                    ctypes.c_double(tolerance),
                    ctypes.c_int(bool(fixDegenerated)),
                    ctypes.c_int(bool(fixSmallEdges)),
                    ctypes.c_int(bool(fixSmallFaces)),
                    ctypes.c_int(bool(sewFaces)),
                    ctypes.c_int(bool(makeSolids)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def convertToNURBS(dimTags: Sequence[tuple[int, int]]) -> None:
            """gmsh.model.occ.convertToNURBS(dimTags)

            Convert the entities `dimTags` to NURBS.

            Types:
            - `dimTags`: vector of pairs of integers
            """
            c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccConvertToNURBS(
                    c_dimTags, c_dimTags_n, ctypes.byref(ierr)
                )

        @staticmethod
        def importShapes(
            fileName: str,
            *,
            highestDimOnly: bool = True,
            format: str = "",  # noqa: A002
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.importShapes(fileName, highestDimOnly=True, format="")

            Import BREP, STEP or IGES shapes from the file `fileName` in the
            OpenCASCADE CAD representation. The imported entities are returned in
            `outDimTags`, as a vector of (dim, tag) pairs. If the optional argument
            `highestDimOnly` is set, only import the highest dimensional entities in
            the file. The optional argument `format` can be used to force the format of
            the file (currently "brep", "step" or "iges").

            Return `outDimTags`.

            Types:
            - `fileName`: string
            - `outDimTags`: vector of pairs of integers
            - `highestDimOnly`: boolean
            - `format`: string
            """
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccImportShapes(
                    ctypes.c_char_p(fileName.encode()),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(bool(highestDimOnly)),
                    ctypes.c_char_p(format.encode()),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def importShapesNativePointer(
            shape: int, *, highestDimOnly: bool = True
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.importShapesNativePointer(shape, highestDimOnly=True)

            Import an OpenCASCADE `shape` by providing a pointer to a native
            OpenCASCADE `TopoDS_Shape` object (passed as a pointer to void). The
            imported entities are returned in `outDimTags` as a vector of (dim, tag)
            pairs. If the optional argument `highestDimOnly` is set, only import the
            highest dimensional entities in `shape`. In Python, this function can be
            used for integration with PythonOCC, in which the SwigPyObject pointer of
            `TopoDS_Shape` must be passed as an int to `shape`, i.e., `shape =
            int(pythonocc_shape.this)'. Warning: this function is unsafe, as providing
            an invalid pointer will lead to undefined behavior.

            Return `outDimTags`.

            Types:
            - `shape`: pointer
            - `outDimTags`: vector of pairs of integers
            - `highestDimOnly`: boolean
            """
            c_outDimTags = ctypes.POINTER(ctypes.c_int)()
            c_outDimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccImportShapesNativePointer(
                    ctypes.c_void_p(shape),
                    ctypes.byref(c_outDimTags),
                    ctypes.byref(c_outDimTags_n),
                    ctypes.c_int(bool(highestDimOnly)),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_outDimTags, c_outDimTags_n.value)

        @staticmethod
        def getEntities(dim: int = -1) -> list[tuple[int, int]]:
            """gmsh.model.occ.getEntities(dim=-1)

            Get all the OpenCASCADE entities. If `dim` is >= 0, return only the
            entities of the specified dimension (e.g. points if `dim` == 0). The
            entities are returned as a vector of (dim, tag) pairs.

            Return `dimTags`.

            Types:
            - `dimTags`: vector of pairs of integers
            - `dim`: integer
            """
            c_dimTags = ctypes.POINTER(ctypes.c_int)()
            c_dimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetEntities(
                    ctypes.byref(c_dimTags),
                    ctypes.byref(c_dimTags_n),
                    ctypes.c_int(dim),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_dimTags, c_dimTags_n.value)

        @staticmethod
        def getEntitiesInBoundingBox(
            xmin: float,
            ymin: float,
            zmin: float,
            xmax: float,
            ymax: float,
            zmax: float,
            *,
            dim: int = -1,
        ) -> list[tuple[int, int]]:
            """gmsh.model.occ.getEntitiesInBoundingBox(xmin, ymin, zmin, xmax, ymax, zmax, dim=-1)

            Get the OpenCASCADE entities in the bounding box defined by the two points
            (`xmin`, `ymin`, `zmin`) and (`xmax`, `ymax`, `zmax`). If `dim` is >= 0,
            return only the entities of the specified dimension (e.g. points if `dim`
            == 0).

            Return `dimTags`.

            Types:
            - `xmin`: double
            - `ymin`: double
            - `zmin`: double
            - `xmax`: double
            - `ymax`: double
            - `zmax`: double
            - `dimTags`: vector of pairs of integers
            - `dim`: integer
            """
            c_dimTags = ctypes.POINTER(ctypes.c_int)()
            c_dimTags_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetEntitiesInBoundingBox(
                    ctypes.c_double(xmin),
                    ctypes.c_double(ymin),
                    ctypes.c_double(zmin),
                    ctypes.c_double(xmax),
                    ctypes.c_double(ymax),
                    ctypes.c_double(zmax),
                    ctypes.byref(c_dimTags),
                    ctypes.byref(c_dimTags_n),
                    ctypes.c_int(dim),
                    ctypes.byref(ierr),
                )

            return _ovectorpair(c_dimTags, c_dimTags_n.value)

        @staticmethod
        def getBoundingBox(
            dim: int, tag: int
        ) -> tuple[float, float, float, float, float, float]:
            """gmsh.model.occ.getBoundingBox(dim, tag)

            Get the bounding box (`xmin`, `ymin`, `zmin`), (`xmax`, `ymax`, `zmax`) of
            the OpenCASCADE entity of dimension `dim` and tag `tag`.

            Return `xmin`, `ymin`, `zmin`, `xmax`, `ymax`, `zmax`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `xmin`: double
            - `ymin`: double
            - `zmin`: double
            - `xmax`: double
            - `ymax`: double
            - `zmax`: double
            """
            c_xmin = ctypes.c_double()
            c_ymin = ctypes.c_double()
            c_zmin = ctypes.c_double()
            c_xmax = ctypes.c_double()
            c_ymax = ctypes.c_double()
            c_zmax = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetBoundingBox(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_xmin),
                    ctypes.byref(c_ymin),
                    ctypes.byref(c_zmin),
                    ctypes.byref(c_xmax),
                    ctypes.byref(c_ymax),
                    ctypes.byref(c_zmax),
                    ctypes.byref(ierr),
                )

            return (
                c_xmin.value,
                c_ymin.value,
                c_zmin.value,
                c_xmax.value,
                c_ymax.value,
                c_zmax.value,
            )

        @staticmethod
        def getCurveLoops(
            surfaceTag: int,
        ) -> tuple[list[int], list[list[int]]]:
            """gmsh.model.occ.getCurveLoops(surfaceTag)

            Get the tags `curveLoopTags` of the curve loops making up the surface of
            tag `surfaceTag`, as well as the tags `curveTags` of the curves making up
            each curve loop.

            Return `curveLoopTags`, `curveTags`.

            Types:
            - `surfaceTag`: integer
            - `curveLoopTags`: vector of integers
            - `curveTags`: vector of vectors of integers
            """
            c_curveLoopTags = ctypes.POINTER(ctypes.c_int)()
            c_curveLoopTags_n = ctypes.c_size_t()
            c_curveTags, c_curveTags_n, c_curveTags_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetCurveLoops(
                    ctypes.c_int(surfaceTag),
                    ctypes.byref(c_curveLoopTags),
                    ctypes.byref(c_curveLoopTags_n),
                    ctypes.byref(c_curveTags),
                    ctypes.byref(c_curveTags_n),
                    ctypes.byref(c_curveTags_nn),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorint(c_curveLoopTags, c_curveLoopTags_n.value),
                _ovectorvectorint(c_curveTags, c_curveTags_n, c_curveTags_nn),
            )

        @staticmethod
        def getSurfaceLoops(
            volumeTag: int,
        ) -> tuple[list[int], list[list[int]]]:
            """gmsh.model.occ.getSurfaceLoops(volumeTag)

            Get the tags `surfaceLoopTags` of the surface loops making up the volume of
            tag `volumeTag`, as well as the tags `surfaceTags` of the surfaces making
            up each surface loop.

            Return `surfaceLoopTags`, `surfaceTags`.

            Types:
            - `volumeTag`: integer
            - `surfaceLoopTags`: vector of integers
            - `surfaceTags`: vector of vectors of integers
            """
            c_surfaceLoopTags = ctypes.POINTER(ctypes.c_int)()
            c_surfaceLoopTags_n = ctypes.c_size_t()
            c_surfaceTags, c_surfaceTags_n, c_surfaceTags_nn = (
                ctypes.POINTER(ctypes.POINTER(ctypes.c_int))(),
                ctypes.POINTER(ctypes.c_size_t)(),
                ctypes.c_size_t(),
            )
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetSurfaceLoops(
                    ctypes.c_int(volumeTag),
                    ctypes.byref(c_surfaceLoopTags),
                    ctypes.byref(c_surfaceLoopTags_n),
                    ctypes.byref(c_surfaceTags),
                    ctypes.byref(c_surfaceTags_n),
                    ctypes.byref(c_surfaceTags_nn),
                    ctypes.byref(ierr),
                )

            return (
                _ovectorint(c_surfaceLoopTags, c_surfaceLoopTags_n.value),
                _ovectorvectorint(
                    c_surfaceTags, c_surfaceTags_n, c_surfaceTags_nn
                ),
            )

        @staticmethod
        def getMass(dim: int, tag: int) -> float:
            """gmsh.model.occ.getMass(dim, tag)

            Get the mass of the OpenCASCADE entity of dimension `dim` and tag `tag`. If
            no density is attached to the entity (the default), the value corresponds
            respectively to the length, area and volume for `dim` = 1, 2 and 3.

            Return `mass`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `mass`: double
            """
            c_mass = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetMass(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_mass),
                    ctypes.byref(ierr),
                )

            return c_mass.value

        @staticmethod
        def getCenterOfMass(dim: int, tag: int) -> tuple[float, float, float]:
            """gmsh.model.occ.getCenterOfMass(dim, tag)

            Get the center of mass of the OpenCASCADE entity of dimension `dim` and tag
            `tag`.

            Return `x`, `y`, `z`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `x`: double
            - `y`: double
            - `z`: double
            """
            c_x = ctypes.c_double()
            c_y = ctypes.c_double()
            c_z = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetCenterOfMass(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_x),
                    ctypes.byref(c_y),
                    ctypes.byref(c_z),
                    ctypes.byref(ierr),
                )

            return (c_x.value, c_y.value, c_z.value)

        @staticmethod
        def getMatrixOfInertia(dim: int, tag: int) -> list[float]:
            """gmsh.model.occ.getMatrixOfInertia(dim, tag)

            Get the matrix of inertia (by row) of the OpenCASCADE entity of dimension
            `dim` and tag `tag`.

            Return `mat`.

            Types:
            - `dim`: integer
            - `tag`: integer
            - `mat`: vector of doubles
            """
            c_mat = ctypes.POINTER(ctypes.c_double)()
            c_mat_n = ctypes.c_size_t()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccGetMatrixOfInertia(
                    ctypes.c_int(dim),
                    ctypes.c_int(tag),
                    ctypes.byref(c_mat),
                    ctypes.byref(c_mat_n),
                    ctypes.byref(ierr),
                )

            return _ovectordouble(c_mat, c_mat_n.value)

        @staticmethod
        def getMaxTag(dim: int) -> int:
            """gmsh.model.occ.getMaxTag(dim)

            Get the maximum tag of entities of dimension `dim` in the OpenCASCADE CAD
            representation.

            Types:
            - `dim`: integer
            """
            with _ErrorCode() as ierr:
                return gmsh.lib.gmshModelOccGetMaxTag(
                    ctypes.c_int(dim), ctypes.byref(ierr)
                )

        @staticmethod
        def setMaxTag(dim: int, maxTag: int) -> None:
            """gmsh.model.occ.setMaxTag(dim, maxTag)

            Set the maximum tag `maxTag` for entities of dimension `dim` in the
            OpenCASCADE CAD representation.

            Types:
            - `dim`: integer
            - `maxTag`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccSetMaxTag(
                    ctypes.c_int(dim), ctypes.c_int(maxTag), ctypes.byref(ierr)
                )

        @staticmethod
        def synchronize() -> None:
            """gmsh.model.occ.synchronize()

            Synchronize the OpenCASCADE CAD representation with the current Gmsh model.
            This can be called at any time, but since it involves a non trivial amount
            of processing, the number of synchronization points should normally be
            minimized. Without synchronization the entities in the OpenCASCADE CAD
            representation are not available to any function outside of the OpenCASCADE
            CAD kernel functions.
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshModelOccSynchronize(ctypes.byref(ierr))

        class mesh:
            """OpenCASCADE CAD kernel meshing constraints"""

            @staticmethod
            def setSize(
                dimTags: Sequence[tuple[int, int]], size: float
            ) -> None:
                """gmsh.model.occ.mesh.setSize(dimTags, size)

                Set a mesh size constraint on the entities `dimTags` (given as a vector of
                (dim, tag) pairs) in the OpenCASCADE CAD representation. Currently only
                entities of dimension 0 (points) are handled.

                Types:
                - `dimTags`: vector of pairs of integers
                - `size`: double
                """
                c_dimTags, c_dimTags_n = _ivectorpair(dimTags)
                with _ErrorCode() as ierr:
                    gmsh.lib.gmshModelOccMeshSetSize(
                        c_dimTags,
                        c_dimTags_n,
                        ctypes.c_double(size),
                        ctypes.byref(ierr),
                    )


class view:
    """Post-processing view functions"""

    @staticmethod
    def add(name: str, *, tag: int = -1) -> int:
        """gmsh.view.add(name, tag=-1)

        Add a new post-processing view, with name `name`. If `tag` is positive use
        it (and remove the view with that tag if it already exists), otherwise
        associate a new tag. Return the view tag.

        Types:
        - `name`: string
        - `tag`: integer
        """
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshViewAdd(
                ctypes.c_char_p(name.encode()),
                ctypes.c_int(tag),
                ctypes.byref(ierr),
            )

    @staticmethod
    def remove(tag: int) -> None:
        """gmsh.view.remove(tag)

        Remove the view with tag `tag`.

        Types:
        - `tag`: integer
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewRemove(ctypes.c_int(tag), ctypes.byref(ierr))

    @staticmethod
    def getIndex(tag: int) -> int:
        """gmsh.view.getIndex(tag)

        Get the index of the view with tag `tag` in the list of currently loaded
        views. This dynamic index (it can change when views are removed) is used to
        access view options.

        Types:
        - `tag`: integer
        """
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshViewGetIndex(
                ctypes.c_int(tag), ctypes.byref(ierr)
            )

    @staticmethod
    def getTags() -> list[int]:
        """gmsh.view.getTags()

        Get the tags of all views.

        Return `tags`.

        Types:
        - `tags`: vector of integers
        """
        c_tags, c_tags_n = (ctypes.POINTER(ctypes.c_int)(), ctypes.c_size_t())
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewGetTags(
                ctypes.byref(c_tags),
                ctypes.byref(c_tags_n),
                ctypes.byref(ierr),
            )
        return _ovectorint(c_tags, c_tags_n.value)

    @staticmethod
    def addModelData(
        tag: int,
        step: int,
        modelName: str,
        dataType: str,
        tags: Sequence[int],
        data: Sequence[Sequence[float]],
        *,
        time: float = 0.0,
        numComponents: int = -1,
        partition: int = 0,
    ) -> None:
        """gmsh.view.addModelData(tag, step, modelName, dataType, tags, data, time=0., numComponents=-1, partition=0)

        Add model-based post-processing data to the view with tag `tag`.
        `modelName` identifies the model the data is attached to. `dataType`
        specifies the type of data, currently either "NodeData", "ElementData" or
        "ElementNodeData". `step` specifies the identifier (>= 0) of the data in a
        sequence. `tags` gives the tags of the nodes or elements in the mesh to
        which the data is associated. `data` is a vector of the same length as
        `tags`: each entry is the vector of double precision numbers representing
        the data associated with the corresponding tag. The optional `time`
        argument associate a time value with the data. `numComponents` gives the
        number of data components (1 for scalar data, 3 for vector data, etc.) per
        entity; if negative, it is automatically inferred (when possible) from the
        input data. `partition` allows one to specify data in several sub-sets.

        Types:
        - `tag`: integer
        - `step`: integer
        - `modelName`: string
        - `dataType`: string
        - `tags`: vector of sizes
        - `data`: vector of vectors of doubles
        - `time`: double
        - `numComponents`: integer
        - `partition`: integer
        """
        c_tags, c_tags_n = _ivectorsize(tags)
        c_data, c_data_n, c_data_nn = _ivectorvectordouble(data)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewAddModelData(
                ctypes.c_int(tag),
                ctypes.c_int(step),
                ctypes.c_char_p(modelName.encode()),
                ctypes.c_char_p(dataType.encode()),
                c_tags,
                c_tags_n,
                c_data,
                c_data_n,
                c_data_nn,
                ctypes.c_double(time),
                ctypes.c_int(numComponents),
                ctypes.c_int(partition),
                ctypes.byref(ierr),
            )

    @staticmethod
    def addHomogeneousModelData(
        tag: int,
        step: int,
        modelName: str,
        dataType: str,
        tags: Sequence[int],
        data: Sequence[float],
        *,
        time: float = 0.0,
        numComponents: int = -1,
        partition: int = 0,
    ) -> None:
        """gmsh.view.addHomogeneousModelData(tag, step, modelName, dataType, tags, data, time=0., numComponents=-1, partition=0)

        Add homogeneous model-based post-processing data to the view with tag
        `tag`. The arguments have the same meaning as in `addModelData`, except
        that `data` is supposed to be homogeneous and is thus flattened in a single
        vector. For data types that can lead to different data sizes per tag (like
        "ElementNodeData"), the data should be padded.

        Types:
        - `tag`: integer
        - `step`: integer
        - `modelName`: string
        - `dataType`: string
        - `tags`: vector of sizes
        - `data`: vector of doubles
        - `time`: double
        - `numComponents`: integer
        - `partition`: integer
        """
        c_tags, c_tags_n = _ivectorsize(tags)
        c_data, c_data_n = _ivectordouble(data)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewAddHomogeneousModelData(
                ctypes.c_int(tag),
                ctypes.c_int(step),
                ctypes.c_char_p(modelName.encode()),
                ctypes.c_char_p(dataType.encode()),
                c_tags,
                c_tags_n,
                c_data,
                c_data_n,
                ctypes.c_double(time),
                ctypes.c_int(numComponents),
                ctypes.c_int(partition),
                ctypes.byref(ierr),
            )

    @staticmethod
    def getModelData(
        tag: int, step: int
    ) -> tuple[str, list[int], list[list[float]], float, int]:
        """gmsh.view.getModelData(tag, step)

        Get model-based post-processing data from the view with tag `tag` at step
        `step`. Return the `data` associated to the nodes or the elements with tags
        `tags`, as well as the `dataType` and the number of components
        `numComponents`.

        Return `dataType`, `tags`, `data`, `time`, `numComponents`.

        Types:
        - `tag`: integer
        - `step`: integer
        - `dataType`: string
        - `tags`: vector of sizes
        - `data`: vector of vectors of doubles
        - `time`: double
        - `numComponents`: integer
        """
        c_dataType = ctypes.c_char_p()
        c_tags, c_tags_n = (
            ctypes.POINTER(ctypes.c_size_t)(),
            ctypes.c_size_t(),
        )
        c_data, c_data_n, c_data_nn = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_double))(),
            ctypes.POINTER(ctypes.c_size_t)(),
            ctypes.c_size_t(),
        )
        c_time = ctypes.c_double()
        c_numComponents = ctypes.c_int()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewGetModelData(
                ctypes.c_int(tag),
                ctypes.c_int(step),
                ctypes.byref(c_dataType),
                ctypes.byref(c_tags),
                ctypes.byref(c_tags_n),
                ctypes.byref(c_data),
                ctypes.byref(c_data_n),
                ctypes.byref(c_data_nn),
                ctypes.byref(c_time),
                ctypes.byref(c_numComponents),
                ctypes.byref(ierr),
            )
        return (
            _ostring(c_dataType),
            _ovectorsize(c_tags, c_tags_n.value),
            _ovectorvectordouble(c_data, c_data_n, c_data_nn),
            c_time.value,
            c_numComponents.value,
        )

    @staticmethod
    def getHomogeneousModelData(
        tag: int, step: int
    ) -> tuple[str, list[int], list[float], float, int]:
        """gmsh.view.getHomogeneousModelData(tag, step)

        Get homogeneous model-based post-processing data from the view with tag
        `tag` at step `step`. The arguments have the same meaning as in
        `getModelData`, except that `data` is returned flattened in a single
        vector, with the appropriate padding if necessary.

        Return `dataType`, `tags`, `data`, `time`, `numComponents`.

        Types:
        - `tag`: integer
        - `step`: integer
        - `dataType`: string
        - `tags`: vector of sizes
        - `data`: vector of doubles
        - `time`: double
        - `numComponents`: integer
        """
        c_dataType = ctypes.c_char_p()
        c_tags, c_tags_n = (
            ctypes.POINTER(ctypes.c_size_t)(),
            ctypes.c_size_t(),
        )
        c_data = ctypes.POINTER(ctypes.c_double)()
        c_data_n = ctypes.c_size_t()
        c_time = ctypes.c_double()
        c_numComponents = ctypes.c_int()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewGetHomogeneousModelData(
                ctypes.c_int(tag),
                ctypes.c_int(step),
                ctypes.byref(c_dataType),
                ctypes.byref(c_tags),
                ctypes.byref(c_tags_n),
                ctypes.byref(c_data),
                ctypes.byref(c_data_n),
                ctypes.byref(c_time),
                ctypes.byref(c_numComponents),
                ctypes.byref(ierr),
            )
        return (
            _ostring(c_dataType),
            _ovectorsize(c_tags, c_tags_n.value),
            _ovectordouble(c_data, c_data_n.value),
            c_time.value,
            c_numComponents.value,
        )

    @staticmethod
    def addListData(
        tag: int, dataType: str, numEle: int, data: Sequence[float]
    ) -> None:
        """gmsh.view.addListData(tag, dataType, numEle, data)

        Add list-based post-processing data to the view with tag `tag`. List-based
        datasets are independent from any model and any mesh. `dataType` identifies
        the data by concatenating the field type ("S" for scalar, "V" for vector,
        "T" for tensor) and the element type ("P" for point, "L" for line, "T" for
        triangle, "S" for tetrahedron, "I" for prism, "H" for hexaHedron, "Y" for
        pyramid). For example `dataType` should be "ST" for a scalar field on
        triangles. `numEle` gives the number of elements in the data. `data`
        contains the data for the `numEle` elements, concatenated, with node
        coordinates followed by values per node, repeated for each step: [e1x1,
        ..., e1xn, e1y1, ..., e1yn, e1z1, ..., e1zn, e1v1..., e1vN, e2x1, ...].

        Types:
        - `tag`: integer
        - `dataType`: string
        - `numEle`: integer
        - `data`: vector of doubles
        """
        c_data, c_data_n = _ivectordouble(data)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewAddListData(
                ctypes.c_int(tag),
                ctypes.c_char_p(dataType.encode()),
                ctypes.c_int(numEle),
                c_data,
                c_data_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def getListData(
        tag: int, *, returnAdaptive: bool = False
    ) -> tuple[list[str], list[int], list[list[float]]]:
        """gmsh.view.getListData(tag, returnAdaptive=False)

        Get list-based post-processing data from the view with tag `tag`. Return
        the types `dataTypes`, the number of elements `numElements` for each data
        type and the `data` for each data type. If `returnAdaptive` is set, return
        the data obtained after adaptive refinement, if available.

        Return `dataType`, `numElements`, `data`.

        Types:
        - `tag`: integer
        - `dataType`: vector of strings
        - `numElements`: vector of integers
        - `data`: vector of vectors of doubles
        - `returnAdaptive`: boolean
        """
        c_dataType, c_dataType_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        c_numElements = ctypes.POINTER(ctypes.c_int)()
        c_numElements_n = ctypes.c_size_t()
        c_data, c_data_n, c_data_nn = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_double))(),
            ctypes.POINTER(ctypes.c_size_t)(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewGetListData(
                ctypes.c_int(tag),
                ctypes.byref(c_dataType),
                ctypes.byref(c_dataType_n),
                ctypes.byref(c_numElements),
                ctypes.byref(c_numElements_n),
                ctypes.byref(c_data),
                ctypes.byref(c_data_n),
                ctypes.byref(c_data_nn),
                ctypes.c_int(bool(returnAdaptive)),
                ctypes.byref(ierr),
            )
        return (
            _ovectorstring(c_dataType, c_dataType_n.value),
            _ovectorint(c_numElements, c_numElements_n.value),
            _ovectorvectordouble(c_data, c_data_n, c_data_nn),
        )

    @staticmethod
    def addListDataString(
        tag: int,
        coord: Sequence[float],
        data: Sequence[str],
        *,
        style: Sequence[str] = (),
    ) -> None:
        """gmsh.view.addListDataString(tag, coord, data, style=[])

        Add a string to a list-based post-processing view with tag `tag`. If
        `coord` contains 3 coordinates the string is positioned in the 3D model
        space ("3D string"); if it contains 2 coordinates it is positioned in the
        2D graphics viewport ("2D string"). `data` contains one or more (for
        multistep views) strings. `style` contains key-value pairs of styling
        parameters, concatenated. Available keys are "Font" (possible values:
        "Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic",
        "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-
        BoldOblique", "Courier", "Courier-Bold", "Courier-Oblique", "Courier-
        BoldOblique", "Symbol", "ZapfDingbats", "Screen"), "FontSize" and "Align"
        (possible values: "Left" or "BottomLeft", "Center" or "BottomCenter",
        "Right" or "BottomRight", "TopLeft", "TopCenter", "TopRight", "CenterLeft",
        "CenterCenter", "CenterRight").

        Types:
        - `tag`: integer
        - `coord`: vector of doubles
        - `data`: vector of strings
        - `style`: vector of strings
        """
        c_coord, c_coord_n = _ivectordouble(coord)
        c_data, c_data_n = _ivectorstring(data)
        c_style, c_style_n = _ivectorstring(style)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewAddListDataString(
                ctypes.c_int(tag),
                c_coord,
                c_coord_n,
                c_data,
                c_data_n,
                c_style,
                c_style_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def getListDataStrings(
        tag: int, dim: int
    ) -> tuple[list[float], list[str], list[str]]:
        """gmsh.view.getListDataStrings(tag, dim)

        Get list-based post-processing data strings (2D strings if `dim` == 2, 3D
        strings if `dim` = 3) from the view with tag `tag`. Return the coordinates
        in `coord`, the strings in `data` and the styles in `style`.

        Return `coord`, `data`, `style`.

        Types:
        - `tag`: integer
        - `dim`: integer
        - `coord`: vector of doubles
        - `data`: vector of strings
        - `style`: vector of strings
        """
        c_coord = ctypes.POINTER(ctypes.c_double)()
        c_coord_n = ctypes.c_size_t()
        c_data, c_data_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        c_style, c_style_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewGetListDataStrings(
                ctypes.c_int(tag),
                ctypes.c_int(dim),
                ctypes.byref(c_coord),
                ctypes.byref(c_coord_n),
                ctypes.byref(c_data),
                ctypes.byref(c_data_n),
                ctypes.byref(c_style),
                ctypes.byref(c_style_n),
                ctypes.byref(ierr),
            )
        return (
            _ovectordouble(c_coord, c_coord_n.value),
            _ovectorstring(c_data, c_data_n.value),
            _ovectorstring(c_style, c_style_n.value),
        )

    @staticmethod
    def setInterpolationMatrices(
        tag: int,
        type: str,  # noqa: A002
        d: int,
        coef: Sequence[float],
        exp: Sequence[float],
        *,
        dGeo: int = 0,
        coefGeo: Sequence[float] = (),
        expGeo: Sequence[float] = (),
    ) -> None:
        """gmsh.view.setInterpolationMatrices(tag, type, d, coef, exp, dGeo=0, coefGeo=[], expGeo=[])

        Set interpolation matrices for the element family `type` ("Line",
        "Triangle", "Quadrangle", "Tetrahedron", "Hexahedron", "Prism", "Pyramid")
        in the view `tag`. The approximation of the values over an element is
        written as a linear combination of `d` basis functions f_i(u, v, w) =
        sum_(j = 0, ..., `d` - 1) `coef`[i][j] u^`exp`[j][0] v^`exp`[j][1]
        w^`exp`[j][2], i = 0, ..., `d`-1, with u, v, w the coordinates in the
        reference element. The `coef` matrix (of size `d` x `d`) and the `exp`
        matrix (of size `d` x 3) are stored as vectors, by row. If `dGeo` is
        positive, use `coefGeo` and `expGeo` to define the interpolation of the x,
        y, z coordinates of the element in terms of the u, v, w coordinates, in
        exactly the same way. If `d` < 0, remove the interpolation matrices.

        Types:
        - `tag`: integer
        - `type`: string
        - `d`: integer
        - `coef`: vector of doubles
        - `exp`: vector of doubles
        - `dGeo`: integer
        - `coefGeo`: vector of doubles
        - `expGeo`: vector of doubles
        """
        c_coef, c_coef_n = _ivectordouble(coef)
        c_exp, c_exp_n = _ivectordouble(exp)
        c_coefGeo, c_coefGeo_n = _ivectordouble(coefGeo)
        c_expGeo, c_expGeo_n = _ivectordouble(expGeo)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewSetInterpolationMatrices(
                ctypes.c_int(tag),
                ctypes.c_char_p(type.encode()),
                ctypes.c_int(d),
                c_coef,
                c_coef_n,
                c_exp,
                c_exp_n,
                ctypes.c_int(dGeo),
                c_coefGeo,
                c_coefGeo_n,
                c_expGeo,
                c_expGeo_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def addAlias(
        refTag: int, *, copyOptions: bool = False, tag: int = -1
    ) -> int:
        """gmsh.view.addAlias(refTag, copyOptions=False, tag=-1)

        Add a post-processing view as an `alias` of the reference view with tag
        `refTag`. If `copyOptions` is set, copy the options of the reference view.
        If `tag` is positive use it (and remove the view with that tag if it
        already exists), otherwise associate a new tag. Return the view tag.

        Types:
        - `refTag`: integer
        - `copyOptions`: boolean
        - `tag`: integer
        """
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshViewAddAlias(
                ctypes.c_int(refTag),
                ctypes.c_int(bool(copyOptions)),
                ctypes.c_int(tag),
                ctypes.byref(ierr),
            )

    @staticmethod
    def combine(
        what: str, how: str, *, remove: bool = True, copyOptions: bool = True
    ) -> None:
        """gmsh.view.combine(what, how, remove=True, copyOptions=True)

        Combine elements (if `what` == "elements") or steps (if `what` == "steps")
        of all views (`how` == "all"), all visible views (`how` == "visible") or
        all views having the same name (`how` == "name"). Remove original views if
        `remove` is set.

        Types:
        - `what`: string
        - `how`: string
        - `remove`: boolean
        - `copyOptions`: boolean
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewCombine(
                ctypes.c_char_p(what.encode()),
                ctypes.c_char_p(how.encode()),
                ctypes.c_int(bool(remove)),
                ctypes.c_int(bool(copyOptions)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def probe(
        tag: int,
        x: float,
        y: float,
        z: float,
        *,
        step: int = -1,
        numComp: int = -1,
        gradient: bool = False,
        distanceMax: float = 0.0,
        xElemCoord: Sequence[float] = (),
        yElemCoord: Sequence[float] = (),
        zElemCoord: Sequence[float] = (),
        dim: int = -1,
    ) -> tuple[list[float], float]:
        """gmsh.view.probe(tag, x, y, z, step=-1, numComp=-1, gradient=False, distanceMax=0., xElemCoord=[], yElemCoord=[], zElemCoord=[], dim=-1)

        Probe the view `tag` for its `values` at point (`x`, `y`, `z`). If no match
        is found, `value` is returned empty. Return only the value at step `step`
        is `step` is positive. Return only values with `numComp` if `numComp` is
        positive. Return the gradient of the `values` if `gradient` is set. If
        `distanceMax` is zero, only return a result if an exact match inside an
        element in the view is found; if `distanceMax` is positive and an exact
        match is not found, return the value at the closest node if it is closer
        than `distanceMax`; if `distanceMax` is negative and an exact match is not
        found, always return the value at the closest node. The distance to the
        match is returned in `distance`. Return the result from the element
        described by its coordinates if `xElementCoord`, `yElementCoord` and
        `zElementCoord` are provided. If `dim` is >= 0, return only matches from
        elements of the specified dimension.

        Return `values`, `distance`.

        Types:
        - `tag`: integer
        - `x`: double
        - `y`: double
        - `z`: double
        - `values`: vector of doubles
        - `distance`: double
        - `step`: integer
        - `numComp`: integer
        - `gradient`: boolean
        - `distanceMax`: double
        - `xElemCoord`: vector of doubles
        - `yElemCoord`: vector of doubles
        - `zElemCoord`: vector of doubles
        - `dim`: integer
        """
        c_values = ctypes.POINTER(ctypes.c_double)()
        c_values_n = ctypes.c_size_t()
        c_distance = ctypes.c_double()
        c_xElemCoord, c_xElemCoord_n = _ivectordouble(xElemCoord)
        c_yElemCoord, c_yElemCoord_n = _ivectordouble(yElemCoord)
        c_zElemCoord, c_zElemCoord_n = _ivectordouble(zElemCoord)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewProbe(
                ctypes.c_int(tag),
                ctypes.c_double(x),
                ctypes.c_double(y),
                ctypes.c_double(z),
                ctypes.byref(c_values),
                ctypes.byref(c_values_n),
                ctypes.byref(c_distance),
                ctypes.c_int(step),
                ctypes.c_int(numComp),
                ctypes.c_int(bool(gradient)),
                ctypes.c_double(distanceMax),
                c_xElemCoord,
                c_xElemCoord_n,
                c_yElemCoord,
                c_yElemCoord_n,
                c_zElemCoord,
                c_zElemCoord_n,
                ctypes.c_int(dim),
                ctypes.byref(ierr),
            )
        return (_ovectordouble(c_values, c_values_n.value), c_distance.value)

    @staticmethod
    def write(tag: int, fileName: str, *, append: bool = False) -> None:
        """gmsh.view.write(tag, fileName, append=False)

        Write the view to a file `fileName`. The export format is determined by the
        file extension. Append to the file if `append` is set.

        Types:
        - `tag`: integer
        - `fileName`: string
        - `append`: boolean
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewWrite(
                ctypes.c_int(tag),
                ctypes.c_char_p(fileName.encode()),
                ctypes.c_int(bool(append)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def setVisibilityPerWindow(
        tag: int, value: int, *, windowIndex: int = 0
    ) -> None:
        """gmsh.view.setVisibilityPerWindow(tag, value, windowIndex=0)

        Set the global visibility of the view `tag` per window to `value`, where
        `windowIndex` identifies the window in the window list.

        Types:
        - `tag`: integer
        - `value`: integer
        - `windowIndex`: integer
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshViewSetVisibilityPerWindow(
                ctypes.c_int(tag),
                ctypes.c_int(value),
                ctypes.c_int(windowIndex),
                ctypes.byref(ierr),
            )

    class option:
        """View option handling functions"""

        @staticmethod
        def setNumber(tag: int, name: str, value: float) -> None:
            """gmsh.view.option.setNumber(tag, name, value)

            Set the numerical option `name` to value `value` for the view with tag
            `tag`.

            Types:
            - `tag`: integer
            - `name`: string
            - `value`: double
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionSetNumber(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.c_double(value),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getNumber(tag: int, name: str) -> float:
            """gmsh.view.option.getNumber(tag, name)

            Get the `value` of the numerical option `name` for the view with tag `tag`.

            Return `value`.

            Types:
            - `tag`: integer
            - `name`: string
            - `value`: double
            """
            c_value = ctypes.c_double()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionGetNumber(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.byref(c_value),
                    ctypes.byref(ierr),
                )

            return c_value.value

        @staticmethod
        def setString(tag: int, name: str, value: str) -> None:
            """gmsh.view.option.setString(tag, name, value)

            Set the string option `name` to value `value` for the view with tag `tag`.

            Types:
            - `tag`: integer
            - `name`: string
            - `value`: string
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionSetString(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.c_char_p(value.encode()),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getString(tag: int, name: str) -> str:
            """gmsh.view.option.getString(tag, name)

            Get the `value` of the string option `name` for the view with tag `tag`.

            Return `value`.

            Types:
            - `tag`: integer
            - `name`: string
            - `value`: string
            """
            c_value = ctypes.c_char_p()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionGetString(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.byref(c_value),
                    ctypes.byref(ierr),
                )

            return _ostring(c_value)

        @staticmethod
        def setColor(
            tag: int, name: str, r: int, g: int, b: int, a: int = 255
        ) -> None:
            """gmsh.view.option.setColor(tag, name, r, g, b, a=255)

            Set the color option `name` to the RGBA value (`r`, `g`, `b`, `a`) for the
            view with tag `tag`, where where `r`, `g`, `b` and `a` should be integers
            between 0 and 255.

            Types:
            - `tag`: integer
            - `name`: string
            - `r`: integer
            - `g`: integer
            - `b`: integer
            - `a`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionSetColor(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.c_int(r),
                    ctypes.c_int(g),
                    ctypes.c_int(b),
                    ctypes.c_int(a),
                    ctypes.byref(ierr),
                )

        @staticmethod
        def getColor(tag: int, name: str) -> tuple[int, int, int, int]:
            """gmsh.view.option.getColor(tag, name)

            Get the `r`, `g`, `b`, `a` value of the color option `name` for the view
            with tag `tag`.

            Return `r`, `g`, `b`, `a`.

            Types:
            - `tag`: integer
            - `name`: string
            - `r`: integer
            - `g`: integer
            - `b`: integer
            - `a`: integer
            """
            c_r = ctypes.c_int()
            c_g = ctypes.c_int()
            c_b = ctypes.c_int()
            c_a = ctypes.c_int()
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionGetColor(
                    ctypes.c_int(tag),
                    ctypes.c_char_p(name.encode()),
                    ctypes.byref(c_r),
                    ctypes.byref(c_g),
                    ctypes.byref(c_b),
                    ctypes.byref(c_a),
                    ctypes.byref(ierr),
                )

            return (c_r.value, c_g.value, c_b.value, c_a.value)

        @staticmethod
        def copy(refTag: int, tag: int) -> None:
            """gmsh.view.option.copy(refTag, tag)

            Copy the options from the view with tag `refTag` to the view with tag
            `tag`.

            Types:
            - `refTag`: integer
            - `tag`: integer
            """
            with _ErrorCode() as ierr:
                gmsh.lib.gmshViewOptionCopy(
                    ctypes.c_int(refTag), ctypes.c_int(tag), ctypes.byref(ierr)
                )


class plugin:
    """Plugin functions"""

    @staticmethod
    def setNumber(name: str, option: str, value: float) -> None:
        """gmsh.plugin.setNumber(name, option, value)

        Set the numerical option `option` to the value `value` for plugin `name`.
        Plugins available in the official Gmsh release are listed in the "Gmsh
        plugins" chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-plugins).

        Types:
        - `name`: string
        - `option`: string
        - `value`: double
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshPluginSetNumber(
                ctypes.c_char_p(name.encode()),
                ctypes.c_char_p(option.encode()),
                ctypes.c_double(value),
                ctypes.byref(ierr),
            )

    @staticmethod
    def setString(name: str, option: str, value: str) -> None:
        """gmsh.plugin.setString(name, option, value)

        Set the string option `option` to the value `value` for plugin `name`.
        Plugins available in the official Gmsh release are listed in the "Gmsh
        plugins" chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-plugins).

        Types:
        - `name`: string
        - `option`: string
        - `value`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshPluginSetString(
                ctypes.c_char_p(name.encode()),
                ctypes.c_char_p(option.encode()),
                ctypes.c_char_p(value.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def run(name: str) -> int:
        """gmsh.plugin.run(name)

        Run the plugin `name`. Return the tag of the created view (if any). Plugins
        available in the official Gmsh release are listed in the "Gmsh plugins"
        chapter of the Gmsh reference manual
        (https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-plugins).

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshPluginRun(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )


class graphics:
    """Graphics functions"""

    @staticmethod
    def draw() -> None:
        """gmsh.graphics.draw()

        Draw all the OpenGL scenes.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshGraphicsDraw(ctypes.byref(ierr))


class fltk:
    """FLTK graphical user interface functions"""

    @staticmethod
    def initialize() -> None:
        """gmsh.fltk.initialize()

        Create the FLTK graphical user interface. Can only be called in the main
        thread.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkInitialize(ctypes.byref(ierr))

    @staticmethod
    def finalize() -> None:
        """gmsh.fltk.finalize()

        Close the FLTK graphical user interface. Can only be called in the main
        thread.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkFinalize(ctypes.byref(ierr))

    @staticmethod
    def wait(time: float = -1.0) -> None:
        """gmsh.fltk.wait(time=-1.)

        Wait at most `time` seconds for user interface events and return. If `time`
        < 0, wait indefinitely. First automatically create the user interface if it
        has not yet been initialized. Can only be called in the main thread.

        Types:
        - `time`: double
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkWait(ctypes.c_double(time), ctypes.byref(ierr))

    @staticmethod
    def update() -> None:
        """gmsh.fltk.update()

        Update the user interface (potentially creating new widgets and windows).
        First automatically create the user interface if it has not yet been
        initialized. Can only be called in the main thread: use `awake("update")'
        to trigger an update of the user interface from another thread.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkUpdate(ctypes.byref(ierr))

    @staticmethod
    def awake(action: str = "") -> None:
        """gmsh.fltk.awake(action="")

        Awake the main user interface thread and process pending events, and
        optionally perform an action (currently the only `action` allowed is
        "update").

        Types:
        - `action`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkAwake(
                ctypes.c_char_p(action.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def lock() -> None:
        """gmsh.fltk.lock()

        Block the current thread until it can safely modify the user interface.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkLock(ctypes.byref(ierr))

    @staticmethod
    def unlock() -> None:
        """gmsh.fltk.unlock()

        Release the lock that was set using lock.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkUnlock(ctypes.byref(ierr))

    @staticmethod
    def run() -> None:
        """gmsh.fltk.run()

        Run the event loop of the graphical user interface, i.e. repeatedly call
        `wait()'. First automatically create the user interface if it has not yet
        been initialized. Can only be called in the main thread.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkRun(ctypes.byref(ierr))

    @staticmethod
    def isAvailable() -> int:
        """gmsh.fltk.isAvailable()

        Check if the user interface is available (e.g. to detect if it has been
        closed).
        """
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshFltkIsAvailable(ctypes.byref(ierr))

    @staticmethod
    def selectEntities(dim: int = -1) -> tuple[int, list[tuple[int, int]]]:
        """gmsh.fltk.selectEntities(dim=-1)

        Select entities in the user interface. Return the selected entities as a
        vector of (dim, tag) pairs. If `dim` is >= 0, return only the entities of
        the specified dimension (e.g. points if `dim` == 0).

        Return an integer, `dimTags`.

        Types:
        - `dimTags`: vector of pairs of integers
        - `dim`: integer
        """
        c_dimTags = ctypes.POINTER(ctypes.c_int)()
        c_dimTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            c_result = gmsh.lib.gmshFltkSelectEntities(
                ctypes.byref(c_dimTags),
                ctypes.byref(c_dimTags_n),
                ctypes.c_int(dim),
                ctypes.byref(ierr),
            )
        return (c_result, _ovectorpair(c_dimTags, c_dimTags_n.value))

    @staticmethod
    def selectElements() -> tuple[int, list[int]]:
        """gmsh.fltk.selectElements()

        Select elements in the user interface.

        Return an integer, `elementTags`.

        Types:
        - `elementTags`: vector of sizes
        """
        c_elementTags, c_elementTags_n = (
            ctypes.POINTER(ctypes.c_size_t)(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            c_result = gmsh.lib.gmshFltkSelectElements(
                ctypes.byref(c_elementTags),
                ctypes.byref(c_elementTags_n),
                ctypes.byref(ierr),
            )
        return (c_result, _ovectorsize(c_elementTags, c_elementTags_n.value))

    @staticmethod
    def selectViews() -> tuple[int, list[int]]:
        """gmsh.fltk.selectViews()

        Select views in the user interface.

        Return an integer, `viewTags`.

        Types:
        - `viewTags`: vector of integers
        """
        c_viewTags = ctypes.POINTER(ctypes.c_int)()
        c_viewTags_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            c_result = gmsh.lib.gmshFltkSelectViews(
                ctypes.byref(c_viewTags),
                ctypes.byref(c_viewTags_n),
                ctypes.byref(ierr),
            )
        return (c_result, _ovectorint(c_viewTags, c_viewTags_n.value))

    @staticmethod
    def splitCurrentWindow(how: str = "v", ratio: float = 0.5) -> None:
        """gmsh.fltk.splitCurrentWindow(how="v", ratio=0.5)

        Split the current window horizontally (if `how` == "h") or vertically (if
        `how` == "v"), using ratio `ratio`. If `how` == "u", restore a single
        window.

        Types:
        - `how`: string
        - `ratio`: double
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkSplitCurrentWindow(
                ctypes.c_char_p(how.encode()),
                ctypes.c_double(ratio),
                ctypes.byref(ierr),
            )

    @staticmethod
    def setCurrentWindow(windowIndex: int = 0) -> None:
        """gmsh.fltk.setCurrentWindow(windowIndex=0)

        Set the current window by speficying its index (starting at 0) in the list
        of all windows. When new windows are created by splits, new windows are
        appended at the end of the list.

        Types:
        - `windowIndex`: integer
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkSetCurrentWindow(
                ctypes.c_int(windowIndex), ctypes.byref(ierr)
            )

    @staticmethod
    def setStatusMessage(message: str, *, graphics: bool = False) -> None:
        """gmsh.fltk.setStatusMessage(message, graphics=False)

        Set a status message in the current window. If `graphics` is set, display
        the message inside the graphic window instead of the status bar.

        Types:
        - `message`: string
        - `graphics`: boolean
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkSetStatusMessage(
                ctypes.c_char_p(message.encode()),
                ctypes.c_int(bool(graphics)),
                ctypes.byref(ierr),
            )

    @staticmethod
    def showContextWindow(dim: int, tag: int) -> None:
        """gmsh.fltk.showContextWindow(dim, tag)

        Show context window for the entity of dimension `dim` and tag `tag`.

        Types:
        - `dim`: integer
        - `tag`: integer
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkShowContextWindow(
                ctypes.c_int(dim), ctypes.c_int(tag), ctypes.byref(ierr)
            )

    @staticmethod
    def openTreeItem(name: str) -> None:
        """gmsh.fltk.openTreeItem(name)

        Open the `name` item in the menu tree.

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkOpenTreeItem(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def closeTreeItem(name: str) -> None:
        """gmsh.fltk.closeTreeItem(name)

        Close the `name` item in the menu tree.

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshFltkCloseTreeItem(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )


class parser:
    """Parser functions"""

    @staticmethod
    def getNames(search: str = "") -> list[str]:
        """gmsh.parser.getNames(search="")

        Get the names of the variables in the Gmsh parser matching the `search`
        regular expression. If `search` is empty, return all the names.

        Return `names`.

        Types:
        - `names`: vector of strings
        - `search`: string
        """
        c_names, c_names_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserGetNames(
                ctypes.byref(c_names),
                ctypes.byref(c_names_n),
                ctypes.c_char_p(search.encode()),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_names, c_names_n.value)

    @staticmethod
    def setNumber(name: str, value: Sequence[float]) -> None:
        """gmsh.parser.setNumber(name, value)

        Set the value of the number variable `name` in the Gmsh parser. Create the
        variable if it does not exist; update the value if the variable exists.

        Types:
        - `name`: string
        - `value`: vector of doubles
        """
        c_value, c_value_n = _ivectordouble(value)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserSetNumber(
                ctypes.c_char_p(name.encode()),
                c_value,
                c_value_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def setString(name: str, value: Sequence[str]) -> None:
        """gmsh.parser.setString(name, value)

        Set the value of the string variable `name` in the Gmsh parser. Create the
        variable if it does not exist; update the value if the variable exists.

        Types:
        - `name`: string
        - `value`: vector of strings
        """
        c_value, c_value_n = _ivectorstring(value)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserSetString(
                ctypes.c_char_p(name.encode()),
                c_value,
                c_value_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def getNumber(name: str) -> list[float]:
        """gmsh.parser.getNumber(name)

        Get the value of the number variable `name` from the Gmsh parser. Return an
        empty vector if the variable does not exist.

        Types:
        - `name`: string
        - `value`: vector of doubles
        """
        c_value = ctypes.POINTER(ctypes.c_double)()
        c_value_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserGetNumber(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_value),
                ctypes.byref(c_value_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_value, c_value_n.value)

    @staticmethod
    def getString(name: str) -> list[str]:
        """gmsh.parser.getString(name)

        Get the value of the string variable `name` from the Gmsh parser. Return an
        empty vector if the variable does not exist.

        Types:
        - `name`: string
        - `value`: vector of strings
        """
        c_value, c_value_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserGetString(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_value),
                ctypes.byref(c_value_n),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_value, c_value_n.value)

    @staticmethod
    def clear(name: str = "") -> None:
        """gmsh.parser.clear(name="")

        Clear all the Gmsh parser variables, or remove a single variable if `name`
        is given.

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserClear(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def parse(fileName: str) -> None:
        """gmsh.parser.parse(fileName)

        Parse the file `fileName` with the Gmsh parser.

        Types:
        - `fileName`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshParserParse(
                ctypes.c_char_p(fileName.encode()), ctypes.byref(ierr)
            )


class onelab:
    """ONELAB server functions"""

    @staticmethod
    def set(data: str, format: str = "json") -> None:  # noqa: A002
        """gmsh.onelab.set(data, format="json")

        Set one or more parameters in the ONELAB database, encoded in `format`.

        Types:
        - `data`: string
        - `format`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabSet(
                ctypes.c_char_p(data.encode()),
                ctypes.c_char_p(format.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def get(name: str = "", format: str = "json") -> str:  # noqa: A002
        """gmsh.onelab.get(name="", format="json")

        Get all the parameters (or a single one if `name` is specified) from the
        ONELAB database, encoded in `format`.

        Return `data`.

        Types:
        - `data`: string
        - `name`: string
        - `format`: string
        """
        c_data = ctypes.c_char_p()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabGet(
                ctypes.byref(c_data),
                ctypes.c_char_p(name.encode()),
                ctypes.c_char_p(format.encode()),
                ctypes.byref(ierr),
            )
        return _ostring(c_data)

    @staticmethod
    def getNames(search: str = "") -> list[str]:
        """gmsh.onelab.getNames(search="")

        Get the names of the parameters in the ONELAB database matching the
        `search` regular expression. If `search` is empty, return all the names.

        Return `names`.

        Types:
        - `names`: vector of strings
        - `search`: string
        """
        c_names, c_names_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabGetNames(
                ctypes.byref(c_names),
                ctypes.byref(c_names_n),
                ctypes.c_char_p(search.encode()),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_names, c_names_n.value)

    @staticmethod
    def setNumber(name: str, value: Sequence[float]) -> None:
        """gmsh.onelab.setNumber(name, value)

        Set the value of the number parameter `name` in the ONELAB database. Create
        the parameter if it does not exist; update the value if the parameter
        exists.

        Types:
        - `name`: string
        - `value`: vector of doubles
        """
        c_value, c_value_n = _ivectordouble(value)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabSetNumber(
                ctypes.c_char_p(name.encode()),
                c_value,
                c_value_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def setString(name: str, value: Sequence[str]) -> None:
        """gmsh.onelab.setString(name, value)

        Set the value of the string parameter `name` in the ONELAB database. Create
        the parameter if it does not exist; update the value if the parameter
        exists.

        Types:
        - `name`: string
        - `value`: vector of strings
        """
        c_value, c_value_n = _ivectorstring(value)
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabSetString(
                ctypes.c_char_p(name.encode()),
                c_value,
                c_value_n,
                ctypes.byref(ierr),
            )

    @staticmethod
    def getNumber(name: str) -> list[float]:
        """gmsh.onelab.getNumber(name)

        Get the value of the number parameter `name` from the ONELAB database.
        Return an empty vector if the parameter does not exist.

        Types:
        - `name`: string
        - `value`: vector of doubles
        """
        c_value = ctypes.POINTER(ctypes.c_double)()
        c_value_n = ctypes.c_size_t()
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabGetNumber(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_value),
                ctypes.byref(c_value_n),
                ctypes.byref(ierr),
            )
        return _ovectordouble(c_value, c_value_n.value)

    @staticmethod
    def getString(name: str) -> list[str]:
        """gmsh.onelab.getString(name)

        Get the value of the string parameter `name` from the ONELAB database.
        Return an empty vector if the parameter does not exist.

        Types:
        - `name`: string
        - `value`: vector of strings
        """
        c_value, c_value_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabGetString(
                ctypes.c_char_p(name.encode()),
                ctypes.byref(c_value),
                ctypes.byref(c_value_n),
                ctypes.byref(ierr),
            )
        return _ovectorstring(c_value, c_value_n.value)

    @staticmethod
    def getChanged(name: str) -> int:
        """gmsh.onelab.getChanged(name)

        Check if any parameters in the ONELAB database used by the client `name`
        have been changed.

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshOnelabGetChanged(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def setChanged(name: str, value: int) -> None:
        """gmsh.onelab.setChanged(name, value)

        Set the changed flag to value `value` for all the parameters in the ONELAB
        database used by the client `name`.

        Types:
        - `name`: string
        - `value`: integer
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabSetChanged(
                ctypes.c_char_p(name.encode()),
                ctypes.c_int(value),
                ctypes.byref(ierr),
            )

    @staticmethod
    def clear(name: str = "") -> None:
        """gmsh.onelab.clear(name="")

        Clear the ONELAB database, or remove a single parameter if `name` is given.

        Types:
        - `name`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabClear(
                ctypes.c_char_p(name.encode()), ctypes.byref(ierr)
            )

    @staticmethod
    def run(name: str = "", command: str = "") -> None:
        """gmsh.onelab.run(name="", command="")

        Run a ONELAB client. If `name` is provided, create a new ONELAB client with
        name `name` and executes `command`. If not, try to run a client that might
        be linked to the processed input files.

        Types:
        - `name`: string
        - `command`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshOnelabRun(
                ctypes.c_char_p(name.encode()),
                ctypes.c_char_p(command.encode()),
                ctypes.byref(ierr),
            )


class logger:
    """Information logging functions"""

    @staticmethod
    def write(message: str, level: str = "info") -> None:
        """gmsh.logger.write(message, level="info")

        Write a `message`. `level` can be "info", "warning" or "error".

        Types:
        - `message`: string
        - `level`: string
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshLoggerWrite(
                ctypes.c_char_p(message.encode()),
                ctypes.c_char_p(level.encode()),
                ctypes.byref(ierr),
            )

    @staticmethod
    def start() -> None:
        """gmsh.logger.start()

        Start logging messages.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshLoggerStart(ctypes.byref(ierr))

    @staticmethod
    def get() -> list[str]:
        """gmsh.logger.get()

        Get logged messages.

        Types:
        - `log`: vector of strings
        """
        c_log, c_log_n = (
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char))(),
            ctypes.c_size_t(),
        )
        with _ErrorCode() as ierr:
            gmsh.lib.gmshLoggerGet(
                ctypes.byref(c_log), ctypes.byref(c_log_n), ctypes.byref(ierr)
            )
        return _ovectorstring(c_log, c_log_n.value)

    @staticmethod
    def stop() -> None:
        """gmsh.logger.stop()

        Stop logging messages.
        """
        with _ErrorCode() as ierr:
            gmsh.lib.gmshLoggerStop(ctypes.byref(ierr))

    @staticmethod
    def getWallTime() -> float:
        """gmsh.logger.getWallTime()

        Return wall clock time (in s).
        """
        gmsh.lib.gmshLoggerGetWallTime.restype = ctypes.c_double
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshLoggerGetWallTime(ctypes.byref(ierr))

    @staticmethod
    def getCpuTime() -> float:
        """gmsh.logger.getCpuTime()

        Return CPU time (in s).
        """
        gmsh.lib.gmshLoggerGetCpuTime.restype = ctypes.c_double
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshLoggerGetCpuTime(ctypes.byref(ierr))

    @staticmethod
    def getMemory() -> float:
        """gmsh.logger.getMemory()

        Return memory usage (in Mb).
        """
        gmsh.lib.gmshLoggerGetMemory.restype = ctypes.c_double
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshLoggerGetMemory(ctypes.byref(ierr))

    @staticmethod
    def getTotalMemory() -> float:
        """gmsh.logger.getTotalMemory()

        Return total available memory (in Mb).
        """
        gmsh.lib.gmshLoggerGetTotalMemory.restype = ctypes.c_double
        with _ErrorCode() as ierr:
            return gmsh.lib.gmshLoggerGetTotalMemory(ctypes.byref(ierr))

    @staticmethod
    def getLastError() -> str:
        """gmsh.logger.getLastError()

        Return last error message, if any.

        Return `error`.

        Types:
        - `error`: string
        """
        c_error = ctypes.c_char_p()
        ierr = ctypes.c_int()
        gmsh.lib.gmshLoggerGetLastError(
            ctypes.byref(c_error), ctypes.byref(ierr)
        )
        if ierr.value != 0:
            msg = "Could not get last error"
            raise RuntimeError(msg)
        return _ostring(c_error)


def _ostring(s: c_char_p) -> str:
    if s.value is None:
        msg = "null pointer"
        raise RuntimeError(msg)
    try:
        return s.value.decode()
    finally:
        gmsh.lib.gmshFree(s)


def _ovectorpair(ptr: _Pointer[c_int], size: int) -> list[tuple[int, int]]:
    # TODO: explain why this function supports odd size
    #   https://github.com/Rupt/tmsh/issues/15
    try:
        return [(ptr[i * 2], ptr[i * 2 + 1]) for i in range(size // 2)]
    finally:
        gmsh.lib.gmshFree(ptr)


def _ovectorint(ptr: _Pointer[c_int], size: int) -> list[int]:
    try:
        return ptr[:size]
    finally:
        gmsh.lib.gmshFree(ptr)


def _ovectorsize(ptr: _Pointer[c_size_t], size: int) -> list[int]:
    try:
        return ptr[:size]
    finally:
        gmsh.lib.gmshFree(ptr)


def _ovectordouble(ptr: _Pointer[c_double], size: int) -> list[float]:
    try:
        return ptr[:size]
    finally:
        gmsh.lib.gmshFree(ptr)


def _ovectorstring(ptr: _Pointer[_Pointer[c_char]], size: int) -> list[str]:
    try:
        return [
            _ostring(ctypes.cast(ptr[i], ctypes.c_char_p)) for i in range(size)
        ]
    finally:
        gmsh.lib.gmshFree(ptr)


def _ovectorvectorint(
    ptr: _Pointer[_Pointer[c_int]],
    size: _Pointer[c_size_t],
    n: ctypes.c_size_t,
) -> list[list[int]]:
    try:
        return [
            _ovectorint(ctypes.pointer(ptr[i].contents), size[i])
            for i in range(n.value)
        ]
    finally:
        gmsh.lib.gmshFree(size)
        gmsh.lib.gmshFree(ptr)


def _ovectorvectorsize(
    ptr: _Pointer[_Pointer[c_size_t]],
    size: _Pointer[c_size_t],
    n: ctypes.c_size_t,
) -> list[list[int]]:
    try:
        return [
            _ovectorsize(ctypes.pointer(ptr[i].contents), size[i])
            for i in range(n.value)
        ]
    finally:
        gmsh.lib.gmshFree(size)
        gmsh.lib.gmshFree(ptr)


def _ovectorvectordouble(
    ptr: _Pointer[_Pointer[c_double]],
    size: _Pointer[c_size_t],
    n: ctypes.c_size_t,
) -> list[list[float]]:
    try:
        return [
            _ovectordouble(ctypes.pointer(ptr[i].contents), size[i])
            for i in range(n.value)
        ]
    finally:
        gmsh.lib.gmshFree(size)
        gmsh.lib.gmshFree(ptr)


def _ovectorvectorpair(
    ptr: _Pointer[_Pointer[c_int]],
    size: _Pointer[c_size_t],
    n: ctypes.c_size_t,
) -> list[list[tuple[int, int]]]:
    try:
        return [_ovectorpair(ptr[i], size[i]) for i in range(n.value)]
    finally:
        gmsh.lib.gmshFree(size)
        gmsh.lib.gmshFree(ptr)


def _ivectorint(o: Sequence[int]) -> tuple[Array[c_int], c_size_t]:
    return (ctypes.c_int * len(o))(*o), ctypes.c_size_t(len(o))


def _ivectorsize(o: Sequence[int]) -> tuple[Array[c_size_t], c_size_t]:
    return (ctypes.c_size_t * len(o))(*o), ctypes.c_size_t(len(o))


def _ivectordouble(o: Sequence[float]) -> tuple[Array[c_double], c_size_t]:
    return (ctypes.c_double * len(o))(*o), ctypes.c_size_t(len(o))


def _ivectorpair(
    o: Sequence[tuple[int, int]],
) -> tuple[Array[Array[c_int]], c_size_t]:
    pairs = ((ctypes.c_int * 2)(a, b) for a, b in o)
    return ((ctypes.c_int * 2) * len(o))(*pairs), ctypes.c_size_t(len(o) * 2)


def _ivectorstring(o: Sequence[str]) -> tuple[Array[c_char_p], c_size_t]:
    array = (ctypes.c_char_p * len(o))(*(s.encode() for s in o))
    size = ctypes.c_size_t(len(o))
    return array, size


def _ivectorvectorsize(
    os: Sequence[Sequence[int]],
) -> tuple[Array[_Pointer[c_size_t]], Array[c_size_t], ctypes.c_size_t]:
    n = len(os)
    parrays = [_ivectorsize(o) for o in os]
    sizes = (ctypes.c_size_t * n)(*(a[1] for a in parrays))
    arrays = (ctypes.POINTER(ctypes.c_size_t) * n)(
        *(ctypes.cast(a[0], ctypes.POINTER(ctypes.c_size_t)) for a in parrays)
    )
    # TODO: avoid illegal attribute assignments
    #   https://github.com/Rupt/tmsh/issues/11
    arrays.ref = [a[0] for a in parrays]  # pyright: ignore [reportAttributeAccessIssue]
    size = ctypes.c_size_t(n)
    return arrays, sizes, size


def _ivectorvectordouble(
    os: Sequence[Sequence[float]],
) -> tuple[Array[_Pointer[c_double]], Array[c_size_t], ctypes.c_size_t]:
    n = len(os)
    parrays = [_ivectordouble(o) for o in os]
    sizes = (ctypes.c_size_t * n)(*(a[1] for a in parrays))
    arrays = (ctypes.POINTER(ctypes.c_double) * n)(
        *(ctypes.cast(a[0], ctypes.POINTER(ctypes.c_double)) for a in parrays)
    )
    # TODO: avoid illegal attribute assignments
    #   https://github.com/Rupt/tmsh/issues/11
    arrays.ref = [a[0] for a in parrays]  # pyright: ignore [reportAttributeAccessIssue]
    size = ctypes.c_size_t(n)
    return arrays, sizes, size


def _iargcargv(o: Sequence[str]) -> tuple[c_int, Array[c_char_p]]:
    argc = ctypes.c_int(len(o))
    argv = (ctypes.c_char_p * len(o))(*(s.encode() for s in o))
    return argc, argv


class _ErrorCode:
    def __init__(self) -> None:
        self._error_code = ctypes.c_int()

    def __enter__(self) -> c_int:
        return self._error_code

    def __exit__(self, *exc: object) -> None:
        del exc  # unused
        if self._error_code.value != 0:
            raise RuntimeError(logger.getLastError())
