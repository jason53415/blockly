/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

/**
 * @fileoverview Classic theme.
 * Contains multi-coloured border to create shadow effect.
 */
'use strict';

goog.provide('Blockly.Themes.Classic');

goog.require('Blockly.Theme');


// Temporary holding object.
Blockly.Themes.Classic = {};

Blockly.Themes.Classic.defaultBlockStyles = {
  "colour_blocks": {
    "colourPrimary": "20"
  },
  "logic_blocks": {
    "colourPrimary": "100"
  },
  "loop_blocks": {
    "colourPrimary": "140"
  },
  "math_blocks": {
    "colourPrimary": "170"
  },
  "text_blocks": {
    "colourPrimary": "190"
  },
  "list_blocks": {
    "colourPrimary": "210"
  },
  "dict_blocks": {
    "colourPrimary": "230"
  },
  "ndarray_blocks": {
    "colourPrimary": "250"
  },
  "model_blocks": {
    "colourPrimary": "270"
  },
  "variable_blocks": {
    "colourPrimary": "290"
  },
  "variable_dynamic_blocks": {
    "colourPrimary": "300"
  },
  "procedure_blocks": {
    "colourPrimary": "310"
  },
  "plot_blocks": {
    "colourPrimary": "335"
  },
  "file_blocks": {
    "colourPrimary": "360"
  },
  "mlgame_blocks": {
    "colourPrimary": "20"
  },
  "hat_blocks": {
    "colourPrimary": "360",
    "hat": "cap"
  }
};

Blockly.Themes.Classic.categoryStyles = {
  "colour_category": {
    "colour": "20"
  },
  "list_category": {
    "colour": "260"
  },
  "logic_category": {
    "colour": "210"
  },
  "loop_category": {
    "colour": "120"
  },
  "math_category": {
    "colour": "230"
  },
  "procedure_category": {
    "colour": "290"
  },
  "text_category": {
    "colour": "160"
  },
  "variable_category": {
    "colour": "330"
  },
  "variable_dynamic_category": {
    "colour": "310"
  }
};

Blockly.Themes.Classic =
    new Blockly.Theme('classic', Blockly.Themes.Classic.defaultBlockStyles,
        Blockly.Themes.Classic.categoryStyles);
