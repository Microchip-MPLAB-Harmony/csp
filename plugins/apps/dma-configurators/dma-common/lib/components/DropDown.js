"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const SymbolAccess_1 = require("@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess");
const dropdown_1 = require("primereact/dropdown");
const react_1 = __importDefault(require("react"));
const CommonUtil_1 = require("@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil");
const Components_1 = require("@mplab_harmony/harmony-plugin-ui/build/components/Components");
let obj = null;
class DropDown extends react_1.default.Component {
    constructor(props) {
        super(props);
        this.componentWillReceiveProps(props);
        obj = this;
        this.props.symbolListeners.forEach(this.Addlistener);
    }
    componentWillReceiveProps(props) {
        this.state = {
            comboSelectedValue: (0, SymbolAccess_1.GetSymbolValue)(props.componentId, props.symbolId),
            comboReadOnlyStatue: props.readOnly,
            comboVisibleState: props.visible,
            comboStyleObjectState: props.styleObject,
            comboclassNameState: props.className,
        };
    }
    Addlistener(value) {
        Components_1.globalSymbolSStateData.set(value, obj);
        (0, SymbolAccess_1.AddSymbolListener)(value);
    }
    updateValue(event) {
        var _a, _b;
        (_b = (_a = this.props).beforeChange) === null || _b === void 0 ? void 0 : _b.call(_a);
        this.changeValue(event.value);
        (0, SymbolAccess_1.UpdateSymbolValue)(this.props.componentId, this.props.symbolId, event.value);
        this.props.onChange(event);
    }
    changeValue(value) {
        if (this.state.comboSelectedValue === value) {
            return;
        }
        this.props.onChange(value);
        this.setState({
            comboSelectedValue: value,
        });
    }
    changeReadOnlyStatus(value) {
        value = (0, CommonUtil_1.convertToBoolean)(value);
        if (this.state.comboReadOnlyStatue === value) {
            return;
        }
        this.setState({
            comboReadOnlyStatue: value,
        });
    }
    changeVisibleStatus(value) {
        value = (0, CommonUtil_1.convertToBoolean)(value);
        if (this.state.comboVisibleState === value) {
            return;
        }
        this.setState({
            comboVisibleState: value,
        });
    }
    changeStyleState(styleObject) {
        this.setState({
            comboStyleObjectState: styleObject,
        });
    }
    changeClassNameState(className) {
        if (this.state.comboclassNameState === className) {
            return;
        }
        this.setState({
            comboclassNameState: className,
        });
    }
    changeComponentState(value, editable, visible) {
        this.changeValue(value);
        this.changeReadOnlyStatus(editable);
        this.changeVisibleStatus(visible);
    }
    render() {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement("div", { className: this.state.comboclassNameState }, this.state.comboVisibleState && (react_1.default.createElement(dropdown_1.Dropdown, { id: this.props.symbolId, style: this.state.comboStyleObjectState, value: this.state.comboSelectedValue, options: this.props.symbolArray, disabled: this.props.readOnly, onChange: (e) => this.updateValue(e) })))));
    }
}
exports.default = DropDown;
