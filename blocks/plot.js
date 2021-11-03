/**
 * @license
 * Copyright 2021 PAIA
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * @fileoverview Plotting blocks for Blockly.
 * @author jason53415@gmail.com (You-Cheng Xiao)
 */
'use strict';

goog.provide('Blockly.Constants.Plot');

goog.require('Blockly');
goog.require('Blockly.Blocks');
goog.require('Blockly.FieldDropdown');
goog.require('Blockly.FieldLabel');
goog.require('Blockly.FieldColour');

Blockly.defineBlocksWithJsonArray([
  // Train a model.
  {
    "type": "plot_plot",
    "message0": "%{BKY_PLOT_PLOT}",
    "args0": [
      {
        "type": "input_value",
        "name": "X"
      },
      {
        "type": "input_value",
        "name": "Y"
      },
      {
        "type": "field_dropdown",
        "name": "MARKER",
        "options": [
          ["None", ""],
          ["\u25CF", "."],
          ["\u25B2", "^"],
          ["\u2605", "*"]
        ]
      },
      {
        "type": "field_dropdown",
        "name": "LINE",
        "options": [
          ["None", ""],
          ["\u23AF\u23AF\u23AF", "-"],
          ["\u207B\u207B\u207B", "--"],
          ["\u2027\u2027\u2027\u2027\u2027", ":"],
          ["\u2012\u2027\u2012", "-."]
        ]
      },
      {
        "type": "field_colour",
        "name": "COLOR",
        "colour": "#1f77b4",
        "colourOptions":
          ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
        "columns": 5
      }
    ],
    "inputsInline": true,
    "previousStatement": null,
    "nextStatement": null,
    "style": "plot_blocks",
    "tooltip": "%{BKY_PLOT_PLOT_TOOLTIP}"
  }
]);
