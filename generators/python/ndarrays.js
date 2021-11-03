/**
 * @license
 * Copyright 2021 PAIA
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * @fileoverview Generating Python for ndarray blocks.
 * @author jason53415@gmail.com (You-Cheng Xiao)
 */
'use strict';

goog.provide('Blockly.Python.Ndarrays');

goog.require('Blockly.Python');

Blockly.Python['ndarrays_create_with'] = function(block) {
  // Create an ndarray of any shape filled with a specific element.
  Blockly.Python.definitions_['import_np'] = 'import numpy as np';
  var shape = new Array(block.dimCount_);
  for (var i = 0; i < block.dimCount_; i++) {
    shape[i] = Blockly.Python.valueToCode(block, 'DIM' + i,
        Blockly.Python.ORDER_NONE) || '0';
  }
  var fill = Blockly.Python.valueToCode(block, 'FILL',
      Blockly.Python.ORDER_NONE) || '0';
  var code = 'np.full((' + shape.join(', ') + '), ' + fill + ')';
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['ndarrays_create_with_list'] = function(block) {
  // Create an ndarray of any shape filled with a specific element.
  Blockly.Python.definitions_['import_np'] = 'import numpy as np';
  var list = Blockly.Python.valueToCode(block, 'LIST',
      Blockly.Python.ORDER_NONE) || '0';
  var code = 'np.array(' + list + ')';
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['ndarrays_to_list'] = function(block) {
  // Create an ndarray of any shape filled with a specific element.
  Blockly.Python.definitions_['import_np'] = 'import numpy as np';
  var array = Blockly.Python.valueToCode(block, 'ARRAY',
      Blockly.Python.ORDER_NONE) || '0';
  var code = array + '.tolist()';
  return [code, Blockly.Python.ORDER_ATOMIC];
};
