"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
<<<<<<< HEAD
const react_1 = require("react");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const FrequencyLabelBySymbolType_1 = __importDefault(require("../LabelComponent/LabelFreqTools/FrequencyLabelBySymbolType"));
const LoadDynamicFreqencyLabels = (props) => {
    const [symbols, setSymbols] = (0, react_1.useState)([]);
    (0, react_1.useEffect)(() => {
        const symbolIDs = props.dynamicLabelSymbolsInfo.map((e) => e.symbol_id);
        harmony_plugin_client_lib_1.symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e) => {
            setSymbols(e);
        });
    }, []);
    return ((0, jsx_runtime_1.jsx)("div", { children: symbols.length !== 0 &&
            props.dynamicLabelSymbolsInfo.map((id, index) => ((0, jsx_runtime_1.jsx)(FrequencyLabelBySymbolType_1.default, { componentId: props.componentId, symbolId: symbols[index].symbolId, className: props.cx(id.class[0]), boldLabelStatus: props.boldLabelStatus, tooltip: props.toolTip, redColorForZeroFrequency: props.redColorForZeroFrequency, symbolType: symbols[index].symbolType }, id.id))) }));
=======
const FrequencyLabelComponent_1 = __importDefault(require("../LabelComponent/FrequencyLabelComponent"));
const LoadDynamicFreqencyLabels = (props) => {
    const symbolIDs = props.dynamicLabelSymbolsInfo.map((e) => e.symbol_id);
    return ((0, jsx_runtime_1.jsx)("div", { children: symbolIDs.length !== 0 &&
            props.dynamicLabelSymbolsInfo.map((id, index) => ((0, jsx_runtime_1.jsx)(FrequencyLabelComponent_1.default, { componentId: props.componentId, symbolId: symbolIDs[index], class: props.cx(id.class[0]), boldLabelStatus: props.boldLabelStatus, redColorForZeroFrequency: props.redColorForZeroFrequency }, id.id))) }));
>>>>>>> 0d345d5887 (Added HTML clock manager PIC32CM_GC_SG supported devices)
};
exports.default = LoadDynamicFreqencyLabels;
