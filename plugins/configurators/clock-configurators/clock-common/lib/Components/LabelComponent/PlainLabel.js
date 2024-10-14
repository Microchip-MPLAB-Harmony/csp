"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const tooltip_1 = require("primereact/tooltip");
const react_1 = require("react");
const uuid_1 = require("uuid");
const PlainLabel = (props) => {
    var _a;
    const [tooltipClass] = (0, react_1.useState)(() => 'x' + (0, uuid_1.v4)());
    return ((0, jsx_runtime_1.jsxs)("div", { children: [(0, jsx_runtime_1.jsx)(tooltip_1.Tooltip, { target: `.${tooltipClass}` }), (0, jsx_runtime_1.jsx)("label", Object.assign({ style: {
                    font: 'Calibri',
                    fontSize: '14px',
                    fontWeight: props.booldStatus ? 'bold' : 'initial',
                    color: props.redColorStatus ? 'red' : 'black'
                }, className: `${tooltipClass} ${(_a = props.className) !== null && _a !== void 0 ? _a : ''}`, "data-pr-tooltip": props.toolTip ? props.toolTip : props.disPlayText, "data-pr-position": 'bottom' }, { children: props.disPlayText }))] }));
};
exports.default = PlainLabel;
