"use strict";
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const button_1 = require("primereact/button");
const dialog_1 = require("primereact/dialog");
const NodeType_1 = require("./NodeType");
const react_1 = require("react");
const MultipleUIComponentsWithLabel_1 = __importDefault(require("./MultipleUIComponentsWithLabel"));
const SettingsDialog = (props) => {
    const [settingDialogStatus, setSettingDialogStatus] = (0, react_1.useState)(false);
    const { componentId, symbolArray, dialogWidth, dialogHeight } = props, expectProps = __rest(props, ["componentId", "symbolArray", "dialogWidth", "dialogHeight"]);
    const footer = ((0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsx)(button_1.Button, { label: 'Close', icon: 'pi pi-check', onClick: () => setSettingDialogStatus(false) }) }));
    return ((0, jsx_runtime_1.jsxs)("div", { children: [(0, jsx_runtime_1.jsx)(NodeType_1.GetIconButton, Object.assign({}, expectProps, { onClick: () => setSettingDialogStatus(true), icon: 'pi pi-cog' })), (0, jsx_runtime_1.jsx)(dialog_1.Dialog, Object.assign({ header: props.tooltip, footer: footer, visible: settingDialogStatus, closeOnEscape: true, dismissableMask: true, resizable: true, position: 'center', modal: true, style: { width: props.dialogWidth, height: props.dialogHeight }, onHide: () => setSettingDialogStatus(false) }, { children: (0, jsx_runtime_1.jsx)("div", { children: (0, jsx_runtime_1.jsx)(MultipleUIComponentsWithLabel_1.default, { componentId: props.componentId, symbolsArray: props.symbolArray }) }) }))] }));
};
exports.default = SettingsDialog;
