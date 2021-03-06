#!/usr/bin/env python

import re

# There are four keyboard layout.
ADJACENCY_GRAPHS = {
    "qwerty": {"!": ["`~", None, None, "2@", "qQ", None], "\"": [";:", "[{", "]}", None, None, "/?"], "#": ["2@", None, None, "4$", "eE", "wW"], "$": ["3#", None, None, "5%", "rR", "eE"], "%": ["4$", None, None, "6^", "tT", "rR"], "&": ["6^", None, None, "8*", "uU", "yY"], "'": [";:", "[{", "]}", None, None, "/?"], "(": ["8*", None, None, "0)", "oO", "iI"], ")": ["9(", None, None, "-_", "pP", "oO"], "*": ["7&", None, None, "9(", "iI", "uU"], "+": ["-_", None, None, None, "]}", "[{"], ",": ["mM", "kK", "lL", ".>", None, None], "-": ["0)", None, None, "=+", "[{", "pP"], ".": [",<", "lL", ";:", "/?", None, None], "/": [".>", ";:", "'\"", None, None, None], "0": ["9(", None, None, "-_", "pP", "oO"], "1": ["`~", None, None, "2@", "qQ", None], "2": ["1!", None, None, "3#", "wW", "qQ"], "3": ["2@", None, None, "4$", "eE", "wW"], "4": ["3#", None, None, "5%", "rR", "eE"], "5": ["4$", None, None, "6^", "tT", "rR"], "6": ["5%", None, None, "7&", "yY", "tT"], "7": ["6^", None, None, "8*", "uU", "yY"], "8": ["7&", None, None, "9(", "iI", "uU"], "9": ["8*", None, None, "0)", "oO", "iI"], ":": ["lL", "pP", "[{", "'\"", "/?", ".>"], ";": ["lL", "pP", "[{", "'\"", "/?", ".>"], "<": ["mM", "kK", "lL", ".>", None, None], "=": ["-_", None, None, None, "]}", "[{"], ">": [",<", "lL", ";:", "/?", None, None], "?": [".>", ";:", "'\"", None, None, None], "@": ["1!", None, None, "3#", "wW", "qQ"], "A": [None, "qQ", "wW", "sS", "zZ", None], "B": ["vV", "gG", "hH", "nN", None, None], "C": ["xX", "dD", "fF", "vV", None, None], "D": ["sS", "eE", "rR", "fF", "cC", "xX"], "E": ["wW", "3#", "4$", "rR", "dD", "sS"], "F": ["dD", "rR", "tT", "gG", "vV", "cC"], "G": ["fF", "tT", "yY", "hH", "bB", "vV"], "H": ["gG", "yY", "uU", "jJ", "nN", "bB"], "I": ["uU", "8*", "9(", "oO", "kK", "jJ"], "J": ["hH", "uU", "iI", "kK", "mM", "nN"], "K": ["jJ", "iI", "oO", "lL", ",<", "mM"], "L": ["kK", "oO", "pP", ";:", ".>", ",<"], "M": ["nN", "jJ", "kK", ",<", None, None], "N": ["bB", "hH", "jJ", "mM", None, None], "O": ["iI", "9(", "0)", "pP", "lL", "kK"], "P": ["oO", "0)", "-_", "[{", ";:", "lL"], "Q": [None, "1!", "2@", "wW", "aA", None], "R": ["eE", "4$", "5%", "tT", "fF", "dD"], "S": ["aA", "wW", "eE", "dD", "xX", "zZ"], "T": ["rR", "5%", "6^", "yY", "gG", "fF"], "U": ["yY", "7&", "8*", "iI", "jJ", "hH"], "V": ["cC", "fF", "gG", "bB", None, None], "W": ["qQ", "2@", "3#", "eE", "sS", "aA"], "X": ["zZ", "sS", "dD", "cC", None, None], "Y": ["tT", "6^", "7&", "uU", "hH", "gG"], "Z": [None, "aA", "sS", "xX", None, None], "[": ["pP", "-_", "=+", "]}", "'\"", ";:"], "\\": ["]}", None, None, None, None, None], "]": ["[{", "=+", None, "\\|", None, "'\""], "^": ["5%", None, None, "7&", "yY", "tT"], "_": ["0)", None, None, "=+", "[{", "pP"], "`": [None, None, None, "1!", None, None], "a": [None, "qQ", "wW", "sS", "zZ", None], "b": ["vV", "gG", "hH", "nN", None, None], "c": ["xX", "dD", "fF", "vV", None, None], "d": ["sS", "eE", "rR", "fF", "cC", "xX"], "e": ["wW", "3#", "4$", "rR", "dD", "sS"], "f": ["dD", "rR", "tT", "gG", "vV", "cC"], "g": ["fF", "tT", "yY", "hH", "bB", "vV"], "h": ["gG", "yY", "uU", "jJ", "nN", "bB"], "i": ["uU", "8*", "9(", "oO", "kK", "jJ"], "j": ["hH", "uU", "iI", "kK", "mM", "nN"], "k": ["jJ", "iI", "oO", "lL", ",<", "mM"], "l": ["kK", "oO", "pP", ";:", ".>", ",<"], "m": ["nN", "jJ", "kK", ",<", None, None], "n": ["bB", "hH", "jJ", "mM", None, None], "o": ["iI", "9(", "0)", "pP", "lL", "kK"], "p": ["oO", "0)", "-_", "[{", ";:", "lL"], "q": [None, "1!", "2@", "wW", "aA", None], "r": ["eE", "4$", "5%", "tT", "fF", "dD"], "s": ["aA", "wW", "eE", "dD", "xX", "zZ"], "t": ["rR", "5%", "6^", "yY", "gG", "fF"], "u": ["yY", "7&", "8*", "iI", "jJ", "hH"], "v": ["cC", "fF", "gG", "bB", None, None], "w": ["qQ", "2@", "3#", "eE", "sS", "aA"], "x": ["zZ", "sS", "dD", "cC", None, None], "y": ["tT", "6^", "7&", "uU", "hH", "gG"], "z": [None, "aA", "sS", "xX", None, None], "{": ["pP", "-_", "=+", "]}", "'\"", ";:"], "|": ["]}", None, None, None, None, None], "}": ["[{", "=+", None, "\\|", None, "'\""], "~": [None, None, None, "1!", None, None]},
    "dvorak": {"!": ["`~", None, None, "2@", "'\"", None], "\"": [None, "1!", "2@", ",<", "aA", None], "#": ["2@", None, None, "4$", ".>", ",<"], "$": ["3#", None, None, "5%", "pP", ".>"], "%": ["4$", None, None, "6^", "yY", "pP"], "&": ["6^", None, None, "8*", "gG", "fF"], "'": [None, "1!", "2@", ",<", "aA", None], "(": ["8*", None, None, "0)", "rR", "cC"], ")": ["9(", None, None, "[{", "lL", "rR"], "*": ["7&", None, None, "9(", "cC", "gG"], "+": ["/?", "]}", None, "\\|", None, "-_"], ",": ["'\"", "2@", "3#", ".>", "oO", "aA"], "-": ["sS", "/?", "=+", None, None, "zZ"], ".": [",<", "3#", "4$", "pP", "eE", "oO"], "/": ["lL", "[{", "]}", "=+", "-_", "sS"], "0": ["9(", None, None, "[{", "lL", "rR"], "1": ["`~", None, None, "2@", "'\"", None], "2": ["1!", None, None, "3#", ",<", "'\""], "3": ["2@", None, None, "4$", ".>", ",<"], "4": ["3#", None, None, "5%", "pP", ".>"], "5": ["4$", None, None, "6^", "yY", "pP"], "6": ["5%", None, None, "7&", "fF", "yY"], "7": ["6^", None, None, "8*", "gG", "fF"], "8": ["7&", None, None, "9(", "cC", "gG"], "9": ["8*", None, None, "0)", "rR", "cC"], ":": [None, "aA", "oO", "qQ", None, None], ";": [None, "aA", "oO", "qQ", None, None], "<": ["'\"", "2@", "3#", ".>", "oO", "aA"], "=": ["/?", "]}", None, "\\|", None, "-_"], ">": [",<", "3#", "4$", "pP", "eE", "oO"], "?": ["lL", "[{", "]}", "=+", "-_", "sS"], "@": ["1!", None, None, "3#", ",<", "'\""], "A": [None, "'\"", ",<", "oO", ";:", None], "B": ["xX", "dD", "hH", "mM", None, None], "C": ["gG", "8*", "9(", "rR", "tT", "hH"], "D": ["iI", "fF", "gG", "hH", "bB", "xX"], "E": ["oO", ".>", "pP", "uU", "jJ", "qQ"], "F": ["yY", "6^", "7&", "gG", "dD", "iI"], "G": ["fF", "7&", "8*", "cC", "hH", "dD"], "H": ["dD", "gG", "cC", "tT", "mM", "bB"], "I": ["uU", "yY", "fF", "dD", "xX", "kK"], "J": ["qQ", "eE", "uU", "kK", None, None], "K": ["jJ", "uU", "iI", "xX", None, None], "L": ["rR", "0)", "[{", "/?", "sS", "nN"], "M": ["bB", "hH", "tT", "wW", None, None], "N": ["tT", "rR", "lL", "sS", "vV", "wW"], "O": ["aA", ",<", ".>", "eE", "qQ", ";:"], "P": [".>", "4$", "5%", "yY", "uU", "eE"], "Q": [";:", "oO", "eE", "jJ", None, None], "R": ["cC", "9(", "0)", "lL", "nN", "tT"], "S": ["nN", "lL", "/?", "-_", "zZ", "vV"], "T": ["hH", "cC", "rR", "nN", "wW", "mM"], "U": ["eE", "pP", "yY", "iI", "kK", "jJ"], "V": ["wW", "nN", "sS", "zZ", None, None], "W": ["mM", "tT", "nN", "vV", None, None], "X": ["kK", "iI", "dD", "bB", None, None], "Y": ["pP", "5%", "6^", "fF", "iI", "uU"], "Z": ["vV", "sS", "-_", None, None, None], "[": ["0)", None, None, "]}", "/?", "lL"], "\\": ["=+", None, None, None, None, None], "]": ["[{", None, None, None, "=+", "/?"], "^": ["5%", None, None, "7&", "fF", "yY"], "_": ["sS", "/?", "=+", None, None, "zZ"], "`": [None, None, None, "1!", None, None], "a": [None, "'\"", ",<", "oO", ";:", None], "b": ["xX", "dD", "hH", "mM", None, None], "c": ["gG", "8*", "9(", "rR", "tT", "hH"], "d": ["iI", "fF", "gG", "hH", "bB", "xX"], "e": ["oO", ".>", "pP", "uU", "jJ", "qQ"], "f": ["yY", "6^", "7&", "gG", "dD", "iI"], "g": ["fF", "7&", "8*", "cC", "hH", "dD"], "h": ["dD", "gG", "cC", "tT", "mM", "bB"], "i": ["uU", "yY", "fF", "dD", "xX", "kK"], "j": ["qQ", "eE", "uU", "kK", None, None], "k": ["jJ", "uU", "iI", "xX", None, None], "l": ["rR", "0)", "[{", "/?", "sS", "nN"], "m": ["bB", "hH", "tT", "wW", None, None], "n": ["tT", "rR", "lL", "sS", "vV", "wW"], "o": ["aA", ",<", ".>", "eE", "qQ", ";:"], "p": [".>", "4$", "5%", "yY", "uU", "eE"], "q": [";:", "oO", "eE", "jJ", None, None], "r": ["cC", "9(", "0)", "lL", "nN", "tT"], "s": ["nN", "lL", "/?", "-_", "zZ", "vV"], "t": ["hH", "cC", "rR", "nN", "wW", "mM"], "u": ["eE", "pP", "yY", "iI", "kK", "jJ"], "v": ["wW", "nN", "sS", "zZ", None, None], "w": ["mM", "tT", "nN", "vV", None, None], "x": ["kK", "iI", "dD", "bB", None, None], "y": ["pP", "5%", "6^", "fF", "iI", "uU"], "z": ["vV", "sS", "-_", None, None, None], "{": ["0)", None, None, "]}", "/?", "lL"], "|": ["=+", None, None, None, None, None], "}": ["[{", None, None, None, "=+", "/?"], "~": [None, None, None, "1!", None, None]},
    "keypad": {"*": ["/", None, None, None, "-", "+", "9", "8"], "+": ["9", "*", "-", None, None, None, None, "6"], "-": ["*", None, None, None, None, None, "+", "9"], ".": ["0", "2", "3", None, None, None, None, None], "/": [None, None, None, None, "*", "9", "8", "7"], "0": [None, "1", "2", "3", ".", None, None, None], "1": [None, None, "4", "5", "2", "0", None, None], "2": ["1", "4", "5", "6", "3", ".", "0", None], "3": ["2", "5", "6", None, None, None, ".", "0"], "4": [None, None, "7", "8", "5", "2", "1", None], "5": ["4", "7", "8", "9", "6", "3", "2", "1"], "6": ["5", "8", "9", "+", None, None, "3", "2"], "7": [None, None, None, "/", "8", "5", "4", None], "8": ["7", None, "/", "*", "9", "6", "5", "4"], "9": ["8", "/", "*", "-", "+", None, "6", "5"]},
    "mac_keypad": {"*": ["/", None, None, None, None, None, "-", "9"], "+": ["6", "9", "-", None, None, None, None, "3"], "-": ["9", "/", "*", None, None, None, "+", "6"], ".": ["0", "2", "3", None, None, None, None, None], "/": ["=", None, None, None, "*", "-", "9", "8"], "0": [None, "1", "2", "3", ".", None, None, None], "1": [None, None, "4", "5", "2", "0", None, None], "2": ["1", "4", "5", "6", "3", ".", "0", None], "3": ["2", "5", "6", "+", None, None, ".", "0"], "4": [None, None, "7", "8", "5", "2", "1", None], "5": ["4", "7", "8", "9", "6", "3", "2", "1"], "6": ["5", "8", "9", "-", "+", None, "3", "2"], "7": [None, None, None, "=", "8", "5", "4", None], "8": ["7", None, "=", "/", "9", "6", "5", "4"], "9": ["8", "=", "/", "*", "-", "+", "6", "5"], "=": [None, None, None, None, "/", "9", "8", "7"]}
}

GRAPHS = {
    'qwerty': ADJACENCY_GRAPHS['qwerty'],
    'dvorak': ADJACENCY_GRAPHS['dvorak'],
    'keypad': ADJACENCY_GRAPHS['keypad'],
    'mac_keypad': ADJACENCY_GRAPHS['mac_keypad'],
}

L33T_TABLE = {
    'a': ['4', '@'],
    'b': ['8'],
    'c': ['(', '{', '[', '<'],
    'e': ['3'],
    'g': ['6', '9'],
    'i': ['1', '!', '|'],
    'l': ['1', '|', '7'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['+', '7'],
    'x': ['%'],
    'z': ['2'],
}

SHIFTED_RX = re.compile(r'[~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?]')


def spatial_match(password, _graphs=GRAPHS, _ranked_dictionaries={}):
    matches = []
    for graph_name, graph in _graphs.items():
        matches.extend(spatial_match_helper(password, graph, graph_name))

    return sorted(matches, key=lambda x: (x['start'], x['end']))


def spatial_match_helper(password, graph, graph_name):
    matches = []
    i = 0
    while i < len(password) - 1:
        j = i + 1
        last_direction = None
        turns = 0
        if graph_name in ['qwerty', 'dvorak', ] and SHIFTED_RX.search(password[i]):
            # initial character is shifted
            shifted_count = 1
        else:
            shifted_count = 0

        while True:
            prev_char = password[j - 1]
            found = False
            # found_direction = -1
            cur_direction = -1
            try:
                adjacents = graph[prev_char] or []
            except KeyError:
                adjacents = []
            # consider growing pattern by one character if j hasn't gone
            # over the edge.
            if j < len(password):
                cur_char = password[j]
                for adj in adjacents:
                    cur_direction += 1
                    if adj and cur_char in adj:
                        found = True
                        found_direction = cur_direction
                        if adj.index(cur_char) == 1:
                            # index 1 in the adjacency means the key is shifted,
                            # 0 means unshifted: A vs a, % vs 5, etc.
                            # for example, 'q' is adjacent to the entry '2@'.
                            # @ is shifted w/ index 1, 2 is unshifted.
                            shifted_count += 1
                        if last_direction != found_direction:
                            # adding a turn is correct even in the initial case
                            # when last_direction is null:
                            # every spatial pattern starts with a turn.
                            turns += 1
                            last_direction = found_direction
                        break
            # if the current pattern continued, extend j and try to grow again
            if found:
                j += 1
            # otherwise push the pattern discovered so far, if any...
            else:
                if j - i > 2:  # don't consider length 1 or 2 chains.
                    matches.append({
                        'pattern': 'spatial',
                        'start': i,
                        'end': j - 1,
                        'token': password[i:j],
                        'graph': graph_name,
                        'turns': turns,
                        'shifted_count': shifted_count,
                    })
                # ...and then start a new search for the rest of the password.
                i = j
                break
    return matches


pwd = 'zxcvfR$321'
res = spatial_match(pwd)
for r in res:
    print(r)

