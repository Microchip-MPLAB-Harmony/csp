"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const PlainLabel = (props) => {
    return ((0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsx)("label", Object.assign({ style: {
                font: 'Calibri',
                fontSize: '14px',
                fontWeight: props.booldStatus ? 'bold' : 'initial'
            }, title: props.toolTip ? props.toolTip : props.disPlayText, className: props.className }, { children: props.disPlayText })) }));
};
exports.default = PlainLabel;
