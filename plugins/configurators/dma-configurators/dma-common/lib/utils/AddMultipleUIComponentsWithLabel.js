"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = __importDefault(require("react"));
const Components_1 = require("../components/Components");
const AddMultipleUIComponentsWithLabel = (props) => {
    function updateValue() {
        props.parentUpdate();
    }
    function GetComponents() {
        return (react_1.default.createElement("div", null, props.symbolsArray.map((object) => (react_1.default.createElement(Components_1.GetUIComponentWithLabel, { componentId: props.componentId, symbolId: object, symbolListeners: [object], onChange: updateValue })))));
    }
    return (react_1.default.createElement("div", null,
        react_1.default.createElement("div", null,
            react_1.default.createElement("div", { className: "p-fluid" },
                react_1.default.createElement(GetComponents, null)))));
};
exports.default = AddMultipleUIComponentsWithLabel;
