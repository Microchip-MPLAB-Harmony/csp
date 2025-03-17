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
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const toast_1 = require("primereact/toast");
const react_1 = require("react");
const NodeType_1 = require("./NodeType");
const confirmdialog_1 = require("primereact/confirmdialog");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const ResetSymbolsIcon = (props) => {
    const toastRef = (0, react_1.useRef)();
    const { componentId, resetSymbolsArray } = props, expectProps = __rest(props, ["componentId", "resetSymbolsArray"]);
    function showToast() {
        toastRef.current.show({
            severity: 'success',
            summary: 'Reset to Default Action Completed!',
            life: 4000
        });
        return null;
    }
    function callConfirmDialog(componentID, _symbolsArray) {
        function acceptAction() {
            harmony_plugin_client_lib_1.symbolUtilApi.clearUserValue(componentID, _symbolsArray);
            showToast();
        }
        (0, confirmdialog_1.confirmDialog)({
            message: 'Are you sure you want to proceed?',
            header: 'Confirmation',
            icon: 'pi pi-exclamation-triangle',
            accept: () => acceptAction(),
            reject: () => null
        });
    }
    function ResetClick() {
        callConfirmDialog(props.componentId, props.resetSymbolsArray);
    }
    return ((0, jsx_runtime_1.jsxs)("div", { children: [(0, jsx_runtime_1.jsx)(toast_1.Toast, { ref: toastRef, position: 'bottom-right' }), (0, jsx_runtime_1.jsx)(NodeType_1.GetIconButton, Object.assign({}, expectProps, { onClick: ResetClick, icon: 'pi pi-refresh' }))] }));
};
exports.default = ResetSymbolsIcon;
