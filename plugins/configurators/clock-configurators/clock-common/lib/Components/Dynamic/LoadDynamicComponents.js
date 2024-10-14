"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const react_1 = require("react");
const LoadDynamicComponents = (props) => {
    const [symbols, setSymbols] = (0, react_1.useState)([]);
    (0, react_1.useEffect)(() => {
        const symbolIDs = props.dynamicSymbolsInfo.map((e) => e.symbol_id);
        harmony_plugin_client_lib_1.symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e) => {
            setSymbols(e);
        });
    }, []);
    return ((0, jsx_runtime_1.jsx)("div", { children: symbols.length !== 0 &&
            props.dynamicSymbolsInfo.map((id, index) => ((0, jsx_runtime_1.jsx)(harmony_plugin_client_lib_1.DefaultControl, { symbol: symbols[index], className: props.cx(id.class[0]) }, id.id))) }));
};
exports.default = LoadDynamicComponents;
