#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module: Exception classes definition

Name: tperrors.py
Exception classes:
    TalosError: base class for application exceptions
    TalosArgumentError: errors in command line arguments
    TalosFileSystemError: errors in saving an image or stats
"""


class TalosError(Exception):
    """Exception class: base class for application exceptions

    Inherit:
        Exception
    Public members:
        Attributes:
            message: string - explanation of the error
            syserror: Exception - system exception
    Special methods:
        __init__: override Exception constructor
    """

    def __init__(self, message):
        """Method: extend Exception constructor

        Inputs:
            message: string - explanation of the error
        """

        self.message = message


class TalosArgumentError(TalosError):
    """Exception class: command line arguments arrors

    Inherit:
        TalosError
    Public members:
        Attributes:
            message: string - explanation of the error
            argument: string - the faulty argument
    Special methods:
        __init__: extend TalosError constructor
    """

    def __init__(self, message, argument):
        """Method: extend Exception constructor

        Inputs:
            argument: string - the faulty argument
            message: string - explanation of the error
        """

        super().__init__(message)
        self.argument = argument


class TalosFileSystemError(TalosError):
    """Exception class: errors in writing on the filesystem.

    Inherit:
        TalosError
    Public members:
        Attributes:
            syserror: Exception - system exception
    Special methods:
        __init__: extend TalosError constructor
    """

    def __init__(self, message, syserror):
        """Method: extend TalosError constructor

        Inputs:
            message: string - explanation of the error
            syserror: Exception - system exception
        """

        super().__init__(message)
        self.syserror = syserror
