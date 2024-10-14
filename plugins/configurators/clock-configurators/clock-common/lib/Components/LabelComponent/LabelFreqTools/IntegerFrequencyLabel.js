"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const PlainLabel_1 = __importDefault(require("../PlainLabel"));
const Tools_1 = require("../../../Tools/Tools");
const IntegerFrequencyLabel = (props) => {
    const clockFreq = (0, harmony_plugin_client_lib_1.useIntegerSymbol)(props);
    return ((0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsx)(PlainLabel_1.default, { disPlayText: (0, Tools_1.GetClockDisplayFreqValue)(clockFreq.value), redColorStatus: (props.redColorForZeroFrequency === true && clockFreq.value === 0) ||
                props.minMaxOutofRangeRedColorStatus === true, booldStatus: props.boldLabelStatus, toolTip: props.tooltip, className: props.className }) }));
};
exports.default = IntegerFrequencyLabel;
