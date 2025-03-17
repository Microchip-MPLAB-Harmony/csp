"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const harmony_plugin_client_lib_2 = require("@mplab_harmony/harmony-plugin-client-lib");
const react_1 = __importDefault(require("react"));
const styled_components_1 = __importDefault(require("styled-components"));
const GridContainer = styled_components_1.default.div `
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  width: 30rem;
`;
const GridItem = styled_components_1.default.div `
  display: flex;
  align-items: center;
`;
const LabelContainer = styled_components_1.default.div `
  justify-content: flex-start;
  max-width: 100%; /* Ensure the label container does not exceed the available space */
  white-space: nowrap; /* Prevent the label from wrapping to the next line */
  overflow: hidden; /* Hide any overflow content */
  text-overflow: ellipsis; /* Display ellipsis (...) for overflow content */
`;
const LabelHidden = styled_components_1.default.div `
  display: none;
`;
const LabelVisible = styled_components_1.default.div `
  display: block;
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
`;
const ComponentHidden = styled_components_1.default.div `
  display: none;
`;
const ComponentVisible = styled_components_1.default.div `
  display: block;
`;
const EmptySpace = styled_components_1.default.div `
  height: 1.5rem;
  visibility: hidden;
`;
const MultipleUIComponentsWithLabel = (props) => {
    const symbolsArray = (0, harmony_plugin_client_lib_1.useSymbols)({
        componentId: props.componentId,
        symbolIds: props.symbolsArray
    });
    return ((0, jsx_runtime_1.jsxs)(GridContainer, { children: [symbolsArray.map((symbol) => symbol.visible && ((0, jsx_runtime_1.jsxs)(react_1.default.Fragment, { children: [(0, jsx_runtime_1.jsx)(GridItem, Object.assign({ className: symbol.label ? 'label-visible' : 'label-hidden' }, { children: (0, jsx_runtime_1.jsx)(LabelContainer, { children: (0, jsx_runtime_1.jsx)("label", { children: symbol.label }) }) })), (0, jsx_runtime_1.jsx)(GridItem, Object.assign({ className: symbol.visible ? 'component-visible' : 'component-hidden' }, { children: (0, jsx_runtime_1.jsx)(harmony_plugin_client_lib_2.DefaultControl, { symbol: symbol }) }))] }, symbol.symbolId))), (0, jsx_runtime_1.jsx)(GridItem, { className: 'empty-space' })] }));
};
exports.default = MultipleUIComponentsWithLabel;
