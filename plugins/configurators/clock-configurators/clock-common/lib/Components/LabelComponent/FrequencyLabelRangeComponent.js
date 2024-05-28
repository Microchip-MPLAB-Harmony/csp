"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const FrequencyLabelRangeComponent = (props) => {
    const clockFreq = (0, harmony_plugin_client_lib_1.useIntegerSymbol)(props);
    return ((0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsxs)("label", Object.assign({ className: props.class, title: props.labelTooltip, style: {
                color: clockFreq.value < props.minValue || clockFreq.value > props.maxValue ? 'red' : 'black',
                fontWeight: props.boldLabelStatus === true ? 'bold' : 'initial'
            } }, { children: [clockFreq.value, " Hz"] })) }));
};
exports.default = FrequencyLabelRangeComponent;
