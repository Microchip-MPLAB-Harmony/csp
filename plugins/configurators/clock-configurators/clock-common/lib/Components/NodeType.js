"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.GetButton = exports.GetIconButton = void 0;
const jsx_runtime_1 = require("react/jsx-runtime");
const button_1 = require("primereact/button");
const GetIconButton = (props) => {
    const newClass = 'p-button-rounded p-button-text p-button-plain p-button-lg p-mr-1 ' + props.className;
    return ((0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsx)(button_1.Button, Object.assign({ tooltipOptions: { position: 'right' }, style: { color: 'black' }, "aria-label": 'Filter' }, props, { className: newClass })) }));
};
exports.GetIconButton = GetIconButton;
function GetButton(props) {
    try {
        return ((0, jsx_runtime_1.jsx)(button_1.Button, Object.assign({ "aria-label": 'Filter', tooltipOptions: { position: 'right' } }, props)));
    }
    catch (err) {
        return (0, jsx_runtime_1.jsx)("div", {});
    }
}
exports.GetButton = GetButton;
