"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
const IntegerFrequencyLabel_1 = __importDefault(require("./IntegerFrequencyLabel"));
const StringFrequencyLabel_1 = __importDefault(require("./StringFrequencyLabel"));
const LongFrequencyLabel_1 = __importDefault(require("./LongFrequencyLabel"));
const FrequencyLabelBySymbolType = (props) => {
    switch (props.symbolType) {
        case 'IntegerSymbol':
            return ((0, jsx_runtime_1.jsx)(jsx_runtime_1.Fragment, { children: (0, jsx_runtime_1.jsx)(IntegerFrequencyLabel_1.default, Object.assign({}, props)) }));
        case 'StringSymbol':
            return ((0, jsx_runtime_1.jsx)(jsx_runtime_1.Fragment, { children: (0, jsx_runtime_1.jsx)(StringFrequencyLabel_1.default, Object.assign({}, props)) }));
        case 'LongSymbol':
            return ((0, jsx_runtime_1.jsx)(jsx_runtime_1.Fragment, { children: (0, jsx_runtime_1.jsx)(LongFrequencyLabel_1.default, Object.assign({}, props)) }));
        default:
            break;
    }
    return null;
};
exports.default = FrequencyLabelBySymbolType;
