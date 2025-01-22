"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const react_1 = require("react");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const FrequencyLabelBySymbolType_1 = __importDefault(require("../LabelComponent/LabelFreqTools/FrequencyLabelBySymbolType"));
const LoadDynamicFreqencyLabels = (props) => {
    try {
        const [symbols, setSymbols] = (0, react_1.useState)([]);
        (0, react_1.useEffect)(() => {
            const symbolIDs = props.dynamicLabelSymbolsInfo.map((e) => e.symbol_id);
            harmony_plugin_client_lib_1.symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e) => {
                setSymbols(e);
            });
        }, []);
        return ((0, jsx_runtime_1.jsx)("div", { children: symbols.length !== 0 &&
                props.dynamicLabelSymbolsInfo.map((id, index) => ((0, jsx_runtime_1.jsx)(FrequencyLabelBySymbolType_1.default, { componentId: props.componentId, symbolId: symbols[index].symbolId, className: props.cx(id.class[0]), boldLabelStatus: props.boldLabelStatus, tooltip: props.toolTip, redColorForZeroFrequency: props.redColorForZeroFrequency, symbolType: symbols[index].symbolType }, id.id))) }));
    }
    catch (error) {
        console.log(error);
        return (0, jsx_runtime_1.jsx)(jsx_runtime_1.Fragment, { children: "Error occurred! " });
    }
};
exports.default = LoadDynamicFreqencyLabels;
