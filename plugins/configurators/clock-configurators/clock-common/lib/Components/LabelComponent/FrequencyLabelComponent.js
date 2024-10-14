"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const react_1 = require("react");
const FrequencyLabelBySymbolType_1 = __importDefault(require("./LabelFreqTools/FrequencyLabelBySymbolType"));
const FrequencyLabelComponent = (props) => {
    const [symbols, setSymbols] = (0, react_1.useState)([]);
    (0, react_1.useEffect)(() => {
        const symbolIDs = [props.symbolId];
        harmony_plugin_client_lib_1.symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e) => {
            setSymbols(e);
        });
    }, []);
    return ((0, jsx_runtime_1.jsx)("div", { children: symbols.length !== 0 && ((0, jsx_runtime_1.jsx)(FrequencyLabelBySymbolType_1.default, Object.assign({ symbolType: symbols[0].symbolType }, props))) }));
};
exports.default = FrequencyLabelComponent;
