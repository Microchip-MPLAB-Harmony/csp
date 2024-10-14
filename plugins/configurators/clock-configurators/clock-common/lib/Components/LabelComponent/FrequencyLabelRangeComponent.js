"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const FrequencyLabelComponent_1 = __importDefault(require("./FrequencyLabelComponent"));
const FrequencyLabelRangeComponent = (props) => {
    const clockFreq = (0, harmony_plugin_client_lib_1.useIntegerSymbol)(props);
    return ((0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsx)(FrequencyLabelComponent_1.default, { redColorForZeroFrequency: clockFreq.value < props.minValue || clockFreq.value > props.maxValue, tooltip: props.labelTooltip, boldLabelStatus: props.boldLabelStatus, class: props.class, componentId: props.componentId, symbolId: props.symbolId }) }));
};
exports.default = FrequencyLabelRangeComponent;
