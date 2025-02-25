#!/usr/bin/python

# Generate .js files defining Blockly core and language messages.
#
# Copyright 2013 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import codecs
import os
import re
import sys
import glob
from common import read_json_file


_NEWLINE_PATTERN = re.compile('[\n\r]')


def string_is_ascii(s):
  try:
    # This approach is better for compatibility
    return all(ord(c) < 128 for c in s)
  except TypeError:
    return False

def load_constants(filename):
  """Read in constants file, which must be output in every language."""
  constant_defs = read_json_file(filename)
  constants_text = '\n'
  for key in constant_defs:
    value = constant_defs[key]
    value = value.replace('"', '\\"')
    constants_text += u'\nBlockly.Msg["{0}"] = \"{1}\";'.format(
        key, value)
  return constants_text

def main():
  """Generate .js files defining Blockly core and language messages."""

  # Process command-line arguments.
  parser = argparse.ArgumentParser(description='Convert JSON files to JS.')
  parser.add_argument('--source_lang', default='en',
                      help='ISO 639-1 source language code')
  parser.add_argument('--source_lang_file',
                      default=os.path.join('json', 'en.json'),
                      help='Path to .json file for source language')
  parser.add_argument('--source_synonym_file',
                      default=os.path.join('json', 'synonyms.json'),
                      help='Path to .json file with synonym definitions')
  parser.add_argument('--source_constants_file',
                      default=os.path.join('json', 'constants.json'),
                      help='Path to .json file with constant definitions')
  parser.add_argument('--output_dir', default='js/',
                      help='relative directory for output files')
  parser.add_argument('--mlgame_dir', default='mlgame/json',
                      help='Path to MLGame .json file with block options')
  parser.add_argument('--mlgame_output_dir', default='mlgame/js/',
                      help='relative directory for output files with block options')
  parser.add_argument('--key_file', default='keys.json',
                      help='relative path to input keys file')
  parser.add_argument('--quiet', action='store_true', default=False,
                      help='do not write anything to standard output')
  parser.add_argument('files', nargs='+', help='input files')
  args = parser.parse_args()
  if not args.output_dir.endswith(os.path.sep):
    args.output_dir += os.path.sep

  # ganerate javascript files of mlgame
  mlgame_files = glob.glob(os.path.join(args.mlgame_dir, "*.json"))
  mlgame_defs = {'en': {}, 'zh-hant': {}}
  for mlgame_file in mlgame_files:
    (_, filename) = os.path.split(mlgame_file)
    game = filename[:filename.index('.')]
    game_options = read_json_file(os.path.join(os.curdir, mlgame_file))

    outname = os.path.join(os.curdir, args.mlgame_output_dir, game + '.js')
    with codecs.open(outname, 'w', 'utf-8') as outfile:
      outfile.write(
            """// This file was automatically generated.  Do not modify.

'use strict';

""")
      if "INIT_INFO" in game_options:
        outfile.write(u'Blockly.Msg["MLPLAY_INIT_INFO_OPTIONS"] = [\n')
        for i, (op, en, zh) in enumerate(game_options["INIT_INFO"]):
          op_name = game.upper() + '_INIT_INFO_' + str(i+1)
          op_key = op
          if i < len(game_options["INIT_INFO"]) - 1:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"],\n'.format(op_name, op_key))
          else:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"]\n'.format(op_name, op_key))
          mlgame_defs['en'][op_name] = en
          mlgame_defs['zh-hant'][op_name] = zh
        outfile.write(u'];\n')

      if "PLAYER_STATUS" in game_options:
        outfile.write(u'Blockly.Msg["MLPLAY_PLAYER_STATUS_OPTIONS"] = [\n')
        for i, (op, en, zh) in enumerate(game_options["PLAYER_STATUS"]):
          op_name = game.upper() + '_PLAYER_STATUS_' + str(i+1)
          op_key = op
          if i < len(game_options["PLAYER_STATUS"]) - 1:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"],\n'.format(op_name, op_key))
          else:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"]\n'.format(op_name, op_key))
          mlgame_defs['en'][op_name] = en
          mlgame_defs['zh-hant'][op_name] = zh
        outfile.write(u'];\n')
      
      if "GAME_STATUS" in game_options:
        outfile.write(u'Blockly.Msg["MLPLAY_GAME_STATUS_OPTIONS"] = [\n')
        for i, (op, en, zh) in enumerate(game_options["GAME_STATUS"]):
          op_name = game.upper() + '_GAME_STATUS_' + str(i+1)
          op_key = op
          if i < len(game_options["GAME_STATUS"]) - 1:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"],\n'.format(op_name, op_key))
          else:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"]\n'.format(op_name, op_key))
          mlgame_defs['en'][op_name] = en
          mlgame_defs['zh-hant'][op_name] = zh
        outfile.write(u'];\n')
      
      if "SCENE_INFO" in game_options:
        outfile.write(u'Blockly.Msg["MLPLAY_GET_INFO_OPTIONS"] = [\n')
        for i, (op, en, zh) in enumerate(game_options["SCENE_INFO"]):
          op_name = game.upper() + '_SCENE_INFO_' + str(i+1)
          op_key = op
          if i < len(game_options["SCENE_INFO"]) - 1:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"],\n'.format(op_name, op_key))
          else:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"]\n'.format(op_name, op_key))
          mlgame_defs['en'][op_name] = en
          mlgame_defs['zh-hant'][op_name] = zh
        outfile.write(u'];\n')
      
      if "CONSTANT" in game_options:
        outfile.write(u'Blockly.Msg["MLPLAY_GET_CONSTANT_OPTIONS"] = [\n')
        for i, (op, en, zh) in enumerate(game_options["CONSTANT"]):
          op_name = game.upper() + '_CONSTANT_' + str(i+1)
          op_key = op
          if i < len(game_options["CONSTANT"]) - 1:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}/{2}"],\n'.format(op_name, i+1, op_key))
          else:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}/{2}"]\n'.format(op_name, i+1, op_key))
          mlgame_defs['en'][op_name] = en
          mlgame_defs['zh-hant'][op_name] = zh
        outfile.write(u'];\n')

      if "ACTION" in game_options:
        outfile.write(u'Blockly.Msg["MLPLAY_RETURN_ACTION_OPTIONS"] = [\n')
        for i, (op, en, zh) in enumerate(game_options["ACTION"]):
          op_name = game.upper() + '_ACTION_' + str(i+1)
          op_key = op
          if i < len(game_options["ACTION"]) - 1:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"],\n'.format(op_name, op_key))
          else:
            outfile.write(u'  ["%{{BKY_{0}}}", "{1}"]\n'.format(op_name, op_key))
          mlgame_defs['en'][op_name] = en
          mlgame_defs['zh-hant'][op_name] = zh
        outfile.write(u'];\n')
    
    if not args.quiet:
      if os.path.isfile(outname):
        print('Created {0}.'.format(outname))
      else:
        print("Failed to create {0}.", outname)

  # Read in source language .json file, which provides any values missing
  # in target languages' .json files.
  source_defs = read_json_file(os.path.join(os.curdir, args.source_lang_file))
  source_defs.update(mlgame_defs['en'])
  # Make sure the source file doesn't contain a newline or carriage return.
  for key, value in source_defs.items():
    if _NEWLINE_PATTERN.search(value):
      print('ERROR: definition of {0} in {1} contained a newline character.'.
            format(key, args.source_lang_file))
      sys.exit(1)
  sorted_keys = sorted(source_defs.keys())

  # Read in synonyms file, which must be output in every language.
  synonym_defs = read_json_file(os.path.join(
      os.curdir, args.source_synonym_file))

  # synonym_defs is also being sorted to ensure the same order is kept
  synonym_text = '\n'.join([u'Blockly.Msg["{0}"] = Blockly.Msg["{1}"];'
      .format(key, synonym_defs[key]) for key in sorted(synonym_defs)])

  # Read in constants file, which must be output in every language.
  constants_text = load_constants(os.path.join(os.curdir, args.source_constants_file))

  # Create each output file.
  for arg_file in args.files:
    (_, filename) = os.path.split(arg_file)
    target_lang = filename[:filename.index('.')]
    if target_lang not in ('qqq', 'keys', 'synonyms', 'constants'):
      target_defs = read_json_file(os.path.join(os.curdir, arg_file))
      if target_lang in ('en', 'zh-hant'):
        target_defs.update(mlgame_defs[target_lang])

      # Verify that keys are 'ascii'
      bad_keys = [key for key in target_defs if not string_is_ascii(key)]
      if bad_keys:
        print(u'These keys in {0} contain non ascii characters: {1}'.format(
            filename, ', '.join(bad_keys)))

      # If there's a '\n' or '\r', remove it and print a warning.
      for key, value in target_defs.items():
        if _NEWLINE_PATTERN.search(value):
          print(u'WARNING: definition of {0} in {1} contained '
                'a newline character.'.
                format(key, arg_file))
          target_defs[key] = _NEWLINE_PATTERN.sub(' ', value)

      # Output file.
      outname = os.path.join(os.curdir, args.output_dir, target_lang + '.js')
      with codecs.open(outname, 'w', 'utf-8') as outfile:
        outfile.write(
            """// This file was automatically generated.  Do not modify.

'use strict';

""".format(target_lang.replace('-', '.')))
        # For each key in the source language file, output the target value
        # if present; otherwise, output the source language value with a
        # warning comment.
        for key in sorted_keys:
          if key in target_defs:
            value = target_defs[key]
            comment = ''
            del target_defs[key]
          else:
            value = source_defs[key]
            comment = '  // untranslated'
          value = value.replace('"', '\\"')
          outfile.write(u'Blockly.Msg["{0}"] = "{1}";{2}\n'
              .format(key, value, comment))

        # Announce any keys defined only for target language.
        if target_defs:
          extra_keys = [key for key in target_defs if key not in synonym_defs]
          synonym_keys = [key for key in target_defs if key in synonym_defs]
          if not args.quiet:
            if extra_keys:
              print(u'These extra keys appeared in {0}: {1}'.format(
                  filename, ', '.join(extra_keys)))
            if synonym_keys:
              print(u'These synonym keys appeared in {0}: {1}'.format(
                  filename, ', '.join(synonym_keys)))

        outfile.write(synonym_text)
        outfile.write(constants_text)

      if not args.quiet:
        print('Created {0}.'.format(outname))


if __name__ == '__main__':
  main()
