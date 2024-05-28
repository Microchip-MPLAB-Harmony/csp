"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const react_1 = require("react");
const FrequencyLabelComponent_1 = __importDefault(require("./FrequencyLabelComponent"));
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const FreqencyLabels = (props) => {
    const [symbols, setSymbols] = (0, react_1.useState)([]);
    (0, react_1.useEffect)(() => {
        const symbolIDs = props.boxInfo.map((e) => e.symbol_id);
        harmony_plugin_client_lib_1.symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e) => {
            setSymbols(e);
        });
    }, []);
    return ((0, jsx_runtime_1.jsx)("div", { children: symbols.length !== 0 &&
            props.boxInfo.map((id, index) => ((0, jsx_runtime_1.jsx)(FrequencyLabelComponent_1.default, { componentId: props.componentId, symbolId: symbols[index].symbolId, class: props.cx(id.class[0]), boldLabelStatus: props.boldLabelStatus, redColorForZeroFrequency: props.redColorForZeroFrequency }, id.id))) }));
};
exports.default = FreqencyLabels;
