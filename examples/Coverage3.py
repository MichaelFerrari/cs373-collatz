#!/usr/bin/env python3

# ------------
# Coverage3.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(3), 8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 run --branch Coverage3.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage3 report -m
Name        Stmts   Miss Branch BrMiss  Cover   Missing
-------------------------------------------------------
Coverage3      16      0      4      0   100%



% python3 -m cProfile coverage3

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
         13386 function calls (13116 primitive calls) in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1000(__init__)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1019(init_module_attrs)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1099(create)
     20/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:1122(_exec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1156(_load_backward_compatible)
     22/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:1186(_load_unlocked)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1266(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1287(load_module)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:129(_new_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1311(is_package)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1336(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:141(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:144(__enter__)
     20/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:1465(exec_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__exit__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:148(<genexpr>)
       20    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap>:1534(get_code)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1591(__init__)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1616(get_filename)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1621(get_data)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1631(path_stats)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:172(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1853(_path_hooks)
       56    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1870(_path_importer_cache)
       20    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:1902(_get_spec)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:192(acquire)
       20    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:1934(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1979(__init__)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1985(<genexpr>)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:2011(_get_spec)
       56    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:2016(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:2061(_fill_cache)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:2102(path_hook_for_FileFinder)
       62    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:2120(__enter__)
       62    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:2124(__exit__)
       22    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:2147(_find_spec)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:217(release)
     22/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:2207(_find_and_load_unlocked)
     22/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:2234(_find_and_load)
    52/44    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:2264(_handle_fromlist)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:257(__init__)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:261(__enter__)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:268(__exit__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:274(_get_module_lock)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:288(cb)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:293(_lock_unlock_module)
     24/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:313(_call_with_frames_removed)
       56    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:34(_relax_case)
       40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:437(cache_from_source)
       40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:45(_r_long)
      358    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:50(_path_join)
      366    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:518(_verbose_message)
      358    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:52(<listcomp>)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:534(_check_name_wrapper)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:546(_requires_builtin_wrapper)
       40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:56(_path_split)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:599(_validate_bytecode_header)
       20    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:654(_compile_bytecode)
      105    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:68(_path_stat)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:728(__init__)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:732(__enter__)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:739(__exit__)
       80    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:742(<genexpr>)
       29    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(_path_is_mode_type)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:790(__init__)
       40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:824(cached)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:842(parent)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:850(has_location)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(spec_from_loader)
       28    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(_path_isfile)
       20    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:884(spec_from_file_location)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:92(_path_isdir)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <string>:5(Match)
        1    0.000    0.000    0.000    0.000 <string>:5(Mismatch)
        1    0.000    0.000    0.000    0.000 <string>:5(TokenInfo)
        1    0.000    0.000    0.000    0.000 <string>:5(_LoggingWatcher)
        1    0.000    0.000    0.000    0.000 Coverage3.py:23(MyUnitTests)
        1    0.000    0.000    0.013    0.013 Coverage3.py:9(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:1043(_StderrHandler)
        1    0.000    0.000    0.000    0.000 __init__.py:1049(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1067(PlaceHolder)
        1    0.000    0.000    0.000    0.000 __init__.py:1111(Manager)
        1    0.000    0.000    0.000    0.000 __init__.py:1116(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1219(Logger)
        1    0.000    0.000    0.000    0.000 __init__.py:1234(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1536(RootLogger)
        1    0.000    0.000    0.000    0.000 __init__.py:1542(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1550(LoggerAdapter)
        2    0.000    0.000    0.000    0.000 __init__.py:182(_checkLevel)
        1    0.000    0.000    0.000    0.000 __init__.py:1898(NullHandler)
        1    0.000    0.000    0.000    0.000 __init__.py:211(_acquireLock)
        1    0.000    0.000    0.000    0.000 __init__.py:220(_releaseLock)
        1    0.000    0.000    0.000    0.000 __init__.py:231(LogRecord)
        1    0.000    0.000    0.003    0.003 __init__.py:24(<module>)
        4    0.000    0.000    0.002    0.000 __init__.py:301(namedtuple)
       17    0.000    0.000    0.000    0.000 __init__.py:364(<genexpr>)
       17    0.000    0.000    0.000    0.000 __init__.py:366(<genexpr>)
        1    0.000    0.000    0.000    0.000 __init__.py:368(PercentStyle)
        1    0.000    0.000    0.000    0.000 __init__.py:374(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:383(StrFormatStyle)
        1    0.000    0.000    0.000    0.000 __init__.py:392(StringTemplateStyle)
        1    0.000    0.000    0.000    0.000 __init__.py:416(Formatter)
        8    0.000    0.000    0.000    0.000 __init__.py:42(normalize_encoding)
        1    0.000    0.000    0.011    0.011 __init__.py:45(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:460(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:589(BufferingFormatter)
        1    0.000    0.000    0.000    0.000 __init__.py:631(Filter)
        1    0.000    0.000    0.000    0.000 __init__.py:668(Filterer)
        2    0.000    0.000    0.000    0.000 __init__.py:673(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:740(_addHandlerRef)
        1    0.000    0.000    0.000    0.000 __init__.py:750(Handler)
        1    0.000    0.000    0.000    0.000 __init__.py:759(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:788(createLock)
        1    0.000    0.000    0.000    0.000 __init__.py:935(StreamHandler)
        1    0.000    0.000    0.000    0.000 __init__.py:986(FileHandler)
       32    0.000    0.000    0.000    0.000 _collections_abc.py:419(get)
        1    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
        1    0.000    0.000    0.000    0.000 _weakrefset.py:81(add)
        1    0.000    0.000    0.000    0.000 argparse.py:1010(_HelpAction)
        2    0.000    0.000    0.000    0.000 argparse.py:1012(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:1029(_VersionAction)
        1    0.000    0.000    0.000    0.000 argparse.py:1055(_SubParsersAction)
        1    0.000    0.000    0.000    0.000 argparse.py:1057(_ChoicesPseudoAction)
        1    0.000    0.000    0.000    0.000 argparse.py:1151(FileType)
        1    0.000    0.000    0.000    0.000 argparse.py:118(_AttributeHolder)
        1    0.000    0.000    0.000    0.000 argparse.py:1205(Namespace)
        1    0.000    0.000    0.000    0.000 argparse.py:1230(_ActionsContainer)
        9    0.000    0.000    0.000    0.000 argparse.py:1232(__init__)
      102    0.000    0.000    0.000    0.000 argparse.py:1284(register)
       28    0.000    0.000    0.000    0.000 argparse.py:1288(_registry_get)
       14    0.000    0.000    0.001    0.000 argparse.py:1313(add_argument)
        6    0.000    0.000    0.000    0.000 argparse.py:1360(add_argument_group)
       24    0.000    0.000    0.000    0.000 argparse.py:1370(_add_action)
        2    0.000    0.000    0.000    0.000 argparse.py:1394(_add_container_actions)
        4    0.000    0.000    0.000    0.000 argparse.py:1434(_get_positional_kwargs)
       10    0.000    0.000    0.000    0.000 argparse.py:1450(_get_optional_kwargs)
       14    0.000    0.000    0.000    0.000 argparse.py:1486(_pop_action_class)
        9    0.000    0.000    0.000    0.000 argparse.py:1490(_get_handler)
       24    0.000    0.000    0.000    0.000 argparse.py:1499(_check_conflict)
        1    0.000    0.000    0.000    0.000 argparse.py:153(HelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:1537(_ArgumentGroup)
        6    0.000    0.000    0.000    0.000 argparse.py:1539(__init__)
       24    0.000    0.000    0.000    0.000 argparse.py:1561(_add_action)
        1    0.000    0.000    0.000    0.000 argparse.py:1571(_MutuallyExclusiveGroup)
        1    0.000    0.000    0.000    0.000 argparse.py:1591(ArgumentParser)
       14    0.000    0.000    0.000    0.000 argparse.py:160(__init__)
        3    0.000    0.000    0.001    0.000 argparse.py:1609(__init__)
       14    0.000    0.000    0.000    0.000 argparse.py:1716(_add_action)
        1    0.000    0.000    0.000    0.000 argparse.py:1728(_get_positional_actions)
        1    0.000    0.000    0.000    0.000 argparse.py:1729(<listcomp>)
        1    0.000    0.000    0.000    0.000 argparse.py:1736(parse_args)
        1    0.000    0.000    0.000    0.000 argparse.py:1743(parse_known_args)
        1    0.000    0.000    0.000    0.000 argparse.py:1778(_parse_known_args)
        1    0.000    0.000    0.000    0.000 argparse.py:1825(take_action)
        1    0.000    0.000    0.000    0.000 argparse.py:1923(consume_positionals)
        1    0.000    0.000    0.000    0.000 argparse.py:203(_Section)
       14    0.000    0.000    0.000    0.000 argparse.py:205(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:2074(_match_arguments_partial)
        1    0.000    0.000    0.000    0.000 argparse.py:2080(<listcomp>)
        1    0.000    0.000    0.000    0.000 argparse.py:2084(<listcomp>)
        1    0.000    0.000    0.000    0.000 argparse.py:2192(_get_nargs_pattern)
        1    0.000    0.000    0.000    0.000 argparse.py:2236(_get_values)
        1    0.000    0.000    0.000    0.000 argparse.py:2314(_check_value)
       14    0.000    0.000    0.000    0.000 argparse.py:2354(_get_formatter)
       14    0.000    0.000    0.000    0.000 argparse.py:565(_metavar_formatter)
       14    0.000    0.000    0.000    0.000 argparse.py:574(format)
       14    0.000    0.000    0.000    0.000 argparse.py:581(_format_args)
        7    0.000    0.000    0.000    0.000 argparse.py:596(<listcomp>)
        1    0.000    0.000    0.000    0.000 argparse.py:62(<module>)
        1    0.000    0.000    0.000    0.000 argparse.py:642(RawDescriptionHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:653(RawTextHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:664(ArgumentDefaultsHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:681(MetavarTypeHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:714(ArgumentError)
        1    0.000    0.000    0.000    0.000 argparse.py:734(ArgumentTypeError)
        1    0.000    0.000    0.000    0.000 argparse.py:743(Action)
       14    0.000    0.000    0.000    0.000 argparse.py:794(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:834(_StoreAction)
        7    0.000    0.000    0.000    0.000 argparse.py:836(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:865(__call__)
        1    0.000    0.000    0.000    0.000 argparse.py:869(_StoreConstAction)
        5    0.000    0.000    0.000    0.000 argparse.py:871(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:892(_StoreTrueAction)
        3    0.000    0.000    0.000    0.000 argparse.py:894(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:909(_StoreFalseAction)
        1    0.000    0.000    0.000    0.000 argparse.py:926(_AppendAction)
        1    0.000    0.000    0.000    0.000 argparse.py:963(_AppendConstAction)
        1    0.000    0.000    0.000    0.000 argparse.py:989(_CountAction)
        1    0.000    0.000    0.005    0.005 case.py:1(<module>)
        1    0.000    0.000    0.000    0.000 case.py:123(_BaseTestCaseContext)
        9    0.000    0.000    0.000    0.000 case.py:1285(_deprecate)
        1    0.000    0.000    0.000    0.000 case.py:1306(FunctionTestCase)
        1    0.000    0.000    0.000    0.000 case.py:133(_AssertRaisesBaseContext)
        1    0.000    0.000    0.000    0.000 case.py:1364(_SubTest)
        1    0.000    0.000    0.000    0.000 case.py:165(_AssertRaisesContext)
        1    0.000    0.000    0.000    0.000 case.py:199(_AssertWarnsContext)
        1    0.000    0.000    0.000    0.000 case.py:24(SkipTest)
        1    0.000    0.000    0.000    0.000 case.py:253(_CapturingHandler)
        1    0.000    0.000    0.000    0.000 case.py:272(_AssertLogsContext)
        1    0.000    0.000    0.000    0.000 case.py:316(TestCase)
        1    0.000    0.000    0.000    0.000 case.py:32(_ShouldStop)
        1    0.000    0.000    0.000    0.000 case.py:37(_UnexpectedSuccess)
        1    0.000    0.000    0.000    0.000 case.py:43(_Outcome)
        2    0.000    0.000    0.000    0.000 contextlib.py:96(contextmanager)
        1    0.000    0.000    0.000    0.000 difflib.py:1652(HtmlDiff)
        1    0.000    0.000    0.001    0.001 difflib.py:27(<module>)
        1    0.000    0.000    0.000    0.000 difflib.py:43(SequenceMatcher)
        1    0.000    0.000    0.000    0.000 difflib.py:751(Differ)
        1    0.000    0.000    0.000    0.000 fnmatch.py:11(<module>)
        1    0.000    0.000    0.000    0.000 functools.py:384(lru_cache)
        1    0.000    0.000    0.000    0.000 functools.py:420(decorating_function)
        6    0.000    0.000    0.000    0.000 functools.py:43(update_wrapper)
        5    0.000    0.000    0.000    0.000 functools.py:73(wraps)
       64    0.000    0.000    0.000    0.000 genericpath.py:16(exists)
       16    0.000    0.000    0.000    0.000 gettext.py:111(_expand_lang)
        8    0.000    0.000    0.001    0.000 gettext.py:353(find)
        8    0.000    0.000    0.001    0.000 gettext.py:408(translation)
        8    0.000    0.000    0.001    0.000 gettext.py:474(dgettext)
        8    0.000    0.000    0.001    0.000 gettext.py:512(gettext)
        1    0.000    0.000    0.002    0.002 linecache.py:6(<module>)
        1    0.000    0.000    0.001    0.001 loader.py:1(<module>)
        1    0.000    0.000    0.000    0.000 loader.py:51(TestLoader)
        1    0.000    0.000    0.000    0.000 loader.py:73(loadTestsFromModule)
        8    0.000    0.000    0.000    0.000 locale.py:339(_replace_encoding)
       16    0.000    0.000    0.000    0.000 locale.py:373(normalize)
        1    0.000    0.000    0.002    0.002 main.py:1(<module>)
        1    0.000    0.000    0.002    0.002 main.py:112(parseArgs)
        1    0.000    0.000    0.000    0.000 main.py:141(createTests)
        1    0.000    0.000    0.002    0.002 main.py:148(_initArgParsers)
        1    0.000    0.000    0.001    0.001 main.py:153(_getParentArgParser)
        1    0.000    0.000    0.000    0.000 main.py:181(_getMainArgParser)
        1    0.000    0.000    0.000    0.000 main.py:192(_getDiscoveryArgParser)
        1    0.000    0.000    0.000    0.000 main.py:227(runTests)
        1    0.000    0.000    0.000    0.000 main.py:48(TestProgram)
        1    0.000    0.000    0.002    0.002 main.py:58(__init__)
       46    0.000    0.000    0.000    0.000 os.py:628(__getitem__)
       46    0.000    0.000    0.000    0.000 os.py:704(encode)
        8    0.000    0.000    0.000    0.000 os.py:708(decode)
        4    0.000    0.000    0.000    0.000 posixpath.py:136(basename)
       68    0.000    0.000    0.000    0.000 posixpath.py:38(_get_sep)
        1    0.000    0.000    0.000    0.000 posixpath.py:49(normcase)
       64    0.000    0.000    0.000    0.000 posixpath.py:70(join)
        1    0.000    0.000    0.000    0.000 pprint.py:101(PrettyPrinter)
        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
        1    0.000    0.000    0.000    0.000 pprint.py:71(_safe_key)
        1    0.000    0.000    0.000    0.000 re.py:157(match)
       44    0.000    0.000    0.003    0.000 re.py:221(compile)
        1    0.000    0.000    0.000    0.000 re.py:239(escape)
       45    0.000    0.000    0.003    0.000 re.py:277(_compile)
        1    0.000    0.000    0.003    0.003 result.py:1(<module>)
        1    0.000    0.000    0.000    0.000 result.py:103(stopTestRun)
        3    0.000    0.000    0.000    0.000 result.py:12(failfast)
        2    0.000    0.000    0.000    0.000 result.py:159(wasSuccessful)
        1    0.000    0.000    0.000    0.000 result.py:24(TestResult)
        1    0.000    0.000    0.000    0.000 result.py:38(__init__)
        1    0.000    0.000    0.000    0.000 result.py:71(startTestRun)
        1    0.000    0.000    0.000    0.000 runner.py:1(<module>)
        1    0.000    0.000    0.000    0.000 runner.py:106(printErrors)
        2    0.000    0.000    0.000    0.000 runner.py:112(printErrorList)
        1    0.000    0.000    0.000    0.000 runner.py:120(TextTestRunner)
        1    0.000    0.000    0.000    0.000 runner.py:128(__init__)
        1    0.000    0.000    0.000    0.000 runner.py:13(_WritelnDecorator)
        1    0.000    0.000    0.000    0.000 runner.py:141(_makeResult)
        1    0.000    0.000    0.000    0.000 runner.py:144(run)
        1    0.000    0.000    0.000    0.000 runner.py:15(__init__)
        8    0.000    0.000    0.000    0.000 runner.py:18(__getattr__)
        4    0.000    0.000    0.000    0.000 runner.py:23(writeln)
        1    0.000    0.000    0.000    0.000 runner.py:29(TextTestResult)
        1    0.000    0.000    0.000    0.000 runner.py:37(__init__)
        1    0.000    0.000    0.000    0.000 signals.py:1(<module>)
        1    0.000    0.000    0.000    0.000 signals.py:42(registerResult)
        1    0.000    0.000    0.000    0.000 signals.py:9(_InterruptHandler)
      200    0.000    0.000    0.000    0.000 sre_compile.py:107(fixup)
       20    0.000    0.000    0.001    0.000 sre_compile.py:227(_compile_charset)
       20    0.001    0.000    0.001    0.000 sre_compile.py:255(_optimize_charset)
        8    0.000    0.000    0.000    0.000 sre_compile.py:406(_mk_bitmap)
        8    0.000    0.000    0.000    0.000 sre_compile.py:408(<listcomp>)
        5    0.000    0.000    0.000    0.000 sre_compile.py:411(_bytes_to_codes)
       19    0.000    0.000    0.000    0.000 sre_compile.py:418(_simple)
        1    0.000    0.000    0.000    0.000 sre_compile.py:423(_generate_overlap_table)
       11    0.000    0.000    0.000    0.000 sre_compile.py:444(_compile_info)
       22    0.000    0.000    0.000    0.000 sre_compile.py:545(isstring)
       11    0.000    0.000    0.001    0.000 sre_compile.py:548(_code)
       11    0.000    0.000    0.003    0.000 sre_compile.py:563(compile)
    46/11    0.000    0.000    0.001    0.000 sre_compile.py:70(_compile)
       70    0.000    0.000    0.000    0.000 sre_parse.py:138(__len__)
        4    0.000    0.000    0.000    0.000 sre_parse.py:140(__delitem__)
      166    0.000    0.000    0.000    0.000 sre_parse.py:142(__getitem__)
       19    0.000    0.000    0.000    0.000 sre_parse.py:146(__setitem__)
       91    0.000    0.000    0.000    0.000 sre_parse.py:150(append)
    65/30    0.000    0.000    0.000    0.000 sre_parse.py:152(getwidth)
       11    0.000    0.000    0.000    0.000 sre_parse.py:190(__init__)
      467    0.000    0.000    0.000    0.000 sre_parse.py:195(__next)
      122    0.000    0.000    0.000    0.000 sre_parse.py:214(match)
      419    0.000    0.000    0.000    0.000 sre_parse.py:220(get)
        1    0.000    0.000    0.000    0.000 sre_parse.py:233(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:235(seek)
        8    0.000    0.000    0.000    0.000 sre_parse.py:265(_class_escape)
       15    0.000    0.000    0.000    0.000 sre_parse.py:307(_escape)
    19/11    0.000    0.000    0.001    0.000 sre_parse.py:363(_parse_sub)
    24/12    0.000    0.000    0.001    0.000 sre_parse.py:441(_parse)
       11    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
        6    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
       11    0.000    0.000    0.000    0.000 sre_parse.py:738(fix_flags)
       11    0.000    0.000    0.001    0.000 sre_parse.py:750(parse)
        6    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
       46    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
        1    0.000    0.000    0.001    0.001 string.py:15(<module>)
        1    0.000    0.000    0.000    0.000 string.py:162(Formatter)
        1    0.000    0.000    0.000    0.000 string.py:51(_TemplateMetaclass)
        1    0.000    0.000    0.001    0.001 string.py:61(__init__)
        1    0.000    0.000    0.000    0.000 string.py:73(Template)
        1    0.000    0.000    0.000    0.000 suite.py:1(<module>)
        1    0.000    0.000    0.000    0.000 suite.py:102(run)
        1    0.000    0.000    0.000    0.000 suite.py:16(BaseTestSuite)
        1    0.000    0.000    0.000    0.000 suite.py:174(_get_previous_module)
        1    0.000    0.000    0.000    0.000 suite.py:21(__init__)
        1    0.000    0.000    0.000    0.000 suite.py:218(_handleModuleTearDown)
        1    0.000    0.000    0.000    0.000 suite.py:243(_tearDownPreviousClass)
        1    0.000    0.000    0.000    0.000 suite.py:270(_ErrorHolder)
        1    0.000    0.000    0.000    0.000 suite.py:317(_DebugResult)
        1    0.000    0.000    0.000    0.000 suite.py:34(__iter__)
        1    0.000    0.000    0.000    0.000 suite.py:54(addTests)
        1    0.000    0.000    0.000    0.000 suite.py:83(__call__)
        1    0.000    0.000    0.000    0.000 suite.py:92(TestSuite)
        1    0.000    0.000    0.000    0.000 threading.py:1(<module>)
        1    0.000    0.000    0.000    0.000 threading.py:1162(Timer)
        1    0.000    0.000    0.000    0.000 threading.py:1192(_MainThread)
        1    0.000    0.000    0.000    0.000 threading.py:1194(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:1211(_DummyThread)
        1    0.000    0.000    0.000    0.000 threading.py:198(Condition)
        1    0.000    0.000    0.000    0.000 threading.py:210(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:249(_is_owned)
        1    0.000    0.000    0.000    0.000 threading.py:329(notify)
        1    0.000    0.000    0.000    0.000 threading.py:352(notify_all)
        1    0.000    0.000    0.000    0.000 threading.py:364(Semaphore)
        1    0.000    0.000    0.000    0.000 threading.py:444(BoundedSemaphore)
        1    0.000    0.000    0.000    0.000 threading.py:482(Event)
        1    0.000    0.000    0.000    0.000 threading.py:493(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:507(set)
        1    0.000    0.000    0.000    0.000 threading.py:570(Barrier)
        1    0.000    0.000    0.000    0.000 threading.py:724(BrokenBarrierError)
        1    0.000    0.000    0.000    0.000 threading.py:742(Thread)
        2    0.000    0.000    0.000    0.000 threading.py:75(RLock)
        1    0.000    0.000    0.000    0.000 threading.py:761(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:88(_RLock)
        1    0.000    0.000    0.000    0.000 threading.py:894(_set_ident)
        1    0.000    0.000    0.000    0.000 threading.py:897(_set_tstate_lock)
        1    0.000    0.000    0.000    0.000 token.py:1(<module>)
        1    0.000    0.000    0.000    0.000 token.py:71(<dictcomp>)
       19    0.000    0.000    0.000    0.000 tokenize.py:109(group)
        1    0.000    0.000    0.000    0.000 tokenize.py:110(any)
        2    0.000    0.000    0.000    0.000 tokenize.py:111(maybe)
        1    0.000    0.000    0.001    0.001 tokenize.py:21(<module>)
        1    0.000    0.000    0.000    0.000 tokenize.py:218(TokenError)
        1    0.000    0.000    0.000    0.000 tokenize.py:220(StopTokenizing)
        1    0.000    0.000    0.000    0.000 tokenize.py:223(Untokenizer)
        1    0.000    0.000    0.000    0.000 tokenize.py:96(TokenInfo)
        1    0.000    0.000    0.002    0.002 traceback.py:1(<module>)
        1    0.000    0.000    0.000    0.000 util.py:1(<module>)
        1    0.000    0.000    0.000    0.000 warnings.py:314(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:32(filterwarnings)
        1    0.000    0.000    0.000    0.000 warnings.py:335(__enter__)
        1    0.000    0.000    0.000    0.000 warnings.py:352(__exit__)
        1    0.000    0.000    0.000    0.000 warnings.py:61(simplefilter)
        1    0.000    0.000    0.000    0.000 weakref.py:101(__init__)
        1    0.000    0.000    0.000    0.000 weakref.py:255(update)
        1    0.000    0.000    0.000    0.000 weakref.py:312(__init__)
        1    0.000    0.000    0.000    0.000 weakref.py:364(__setitem__)
    97/95    0.001    0.000    0.003    0.000 {built-in method __build_class__}
        3    0.000    0.000    0.001    0.000 {built-in method __import__}
        4    0.000    0.000    0.000    0.000 {built-in method _filters_mutated}
       20    0.000    0.000    0.000    0.000 {built-in method _fix_co_filename}
        4    0.000    0.000    0.000    0.000 {built-in method _getframe}
        1    0.000    0.000    0.000    0.000 {built-in method _set_sentinel}
       62    0.000    0.000    0.000    0.000 {built-in method acquire_lock}
       46    0.000    0.000    0.000    0.000 {built-in method allocate_lock}
       22    0.000    0.000    0.000    0.000 {built-in method any}
       28    0.000    0.000    0.000    0.000 {built-in method callable}
       22    0.000    0.000    0.000    0.000 {built-in method chr}
       11    0.000    0.000    0.000    0.000 {built-in method compile}
        1    0.000    0.000    0.000    0.000 {built-in method dir}
     25/1    0.001    0.000    0.013    0.013 {built-in method exec}
        1    0.000    0.000    0.000    0.000 {built-in method exit}
       40    0.000    0.000    0.000    0.000 {built-in method from_bytes}
       63    0.000    0.000    0.000    0.000 {built-in method get_ident}
      191    0.000    0.000    0.000    0.000 {built-in method getattr}
       24    0.000    0.000    0.000    0.000 {built-in method getcwd}
      232    0.000    0.000    0.000    0.000 {built-in method getlower}
        1    0.000    0.000    0.000    0.000 {built-in method globals}
      202    0.000    0.000    0.000    0.000 {built-in method hasattr}
        2    0.000    0.000    0.000    0.000 {built-in method init_builtin}
       14    0.000    0.000    0.000    0.000 {built-in method is_builtin}
       20    0.000    0.000    0.000    0.000 {built-in method is_frozen}
      535    0.000    0.000    0.000    0.000 {built-in method isinstance}
        2    0.000    0.000    0.000    0.000 {built-in method issubclass}
        2    0.000    0.000    0.000    0.000 {built-in method iter}
1405/1383    0.000    0.000    0.000    0.000 {built-in method len}
        1    0.000    0.000    0.000    0.000 {built-in method listdir}
       20    0.002    0.000    0.002    0.000 {built-in method loads}
       22    0.000    0.000    0.000    0.000 {built-in method max}
      114    0.000    0.000    0.000    0.000 {built-in method min}
       73    0.000    0.000    0.000    0.000 {built-in method ord}
        1    0.000    0.000    0.000    0.000 {built-in method register}
       93    0.000    0.000    0.000    0.000 {built-in method release_lock}
        4    0.000    0.000    0.000    0.000 {built-in method repr}
       40    0.000    0.000    0.000    0.000 {built-in method setattr}
      169    0.000    0.000    0.000    0.000 {built-in method stat}
        3    0.000    0.000    0.000    0.000 {built-in method time}
       17    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        3    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.lock' objects}
       16    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
      859    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        5    0.000    0.000    0.000    0.000 {method 'cast' of 'memoryview' objects}
        8    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       46    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
      212    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       17    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       66    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
       48    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      338    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
      139    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'groups' of '_sre.SRE_Match' objects}
        8    0.000    0.000    0.000    0.000 {method 'index' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
       40    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
       21    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
       12    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
      443    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       32    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
       41    0.000    0.000    0.000    0.000 {method 'match' of '_sre.SRE_Pattern' objects}
       24    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       20    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
        1    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 {method 'release' of '_thread.lock' objects}
        7    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
       25    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       16    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        4    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      184    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
      756    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      120    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
       20    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
      263    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'tolist' of 'memoryview' objects}
        8    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
        8    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
"""
