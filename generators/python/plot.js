/**
 * @license
 * Copyright 2021 PAIA
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * @fileoverview Generating Python for plotting blocks.
 * @author jason53415@gmail.com (You-Cheng Xiao)
 */
'use strict';

goog.provide('Blockly.Python.Plot');

goog.require('Blockly.Python');

Blockly.Python['plot_plot'] = function(block) {
  // Plot.
  Blockly.Python.definitions_['import_plt'] = 'import matplotlib.pyplot as plt';
  var x = Blockly.Python.valueToCode(block, 'X',
      Blockly.Python.ORDER_NONE) || '[]';
  var y = Blockly.Python.valueToCode(block, 'Y',
      Blockly.Python.ORDER_NONE) || '[]';
  var marker = block.getFieldValue('MARKER');
  var line = block.getFieldValue('LINE');
  var color = block.getFieldValue('COLOR');
  var code = 'plt.plot(' + x + ', ' + y + ', "' + marker + line + '", color="' + color + '")\n' +
              'plt.show()\n';
  return code;
};
