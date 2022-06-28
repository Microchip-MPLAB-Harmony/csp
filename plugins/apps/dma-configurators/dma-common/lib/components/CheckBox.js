"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const SymbolAccess_1 = require("@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess");
const checkbox_1 = require("primereact/checkbox");
const react_1 = __importDefault(require("react"));
const CommonUtil_1 = require("@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil");
const Components_1 = require("@mplab_harmony/harmony-plugin-ui/build/components/Components");
let obj = null;
class CheckBox extends react_1.default.Component {
    constructor(props) {
        super(props);
        this.componentWillReceiveProps(props);
        obj = this;
        this.props.symbolListeners.forEach(this.Addlistener);
    }
    componentWillReceiveProps(props) {
        this.state = {
            checkBoxstatus: (0, CommonUtil_1.convertToBoolean)(props.symbolValue),
            checkBoxReadOnlyState: props.readOnly,
            checkBoxVisibleState: props.visible,
            checkboxStyleObjectState: props.styleObject,
            checkBoxclassNameState: props.className,
        };
    }
    Addlistener(value) {
        Components_1.globalSymbolSStateData.set(value, obj);
        (0, SymbolAccess_1.AddSymbolListener)(value);
    }
    updateValue(checked) {
        var _a, _b;
        (_b = (_a = this.props).beforeChange) === null || _b === void 0 ? void 0 : _b.call(_a);
        this.changeValue(checked);
        (0, SymbolAccess_1.UpdateSymbolValue)(this.props.componentId, this.props.symbolId, checked);
        this.props.onChange(checked);
    }
    changeValue(value) {
        value = (0, CommonUtil_1.convertToBoolean)(value);
        if (this.state.checkBoxstatus === value) {
            return;
        }
        this.props.onChange(value);
        this.setState({
            checkBoxstatus: value,
        });
    }
    changeReadOnlyStatus(value) {
        value = (0, CommonUtil_1.convertToBoolean)(value);
        if (this.state.checkBoxReadOnlyState === value) {
            return;
        }
        this.setState({
            checkBoxReadOnlyState: value,
        });
    }
    changeVisibleStatus(value) {
        value = (0, CommonUtil_1.convertToBoolean)(value);
        if (this.state.checkBoxVisibleState === value) {
            return;
        }
        this.setState({
            checkBoxVisibleState: value,
        });
    }
    changeStyleState(styleObject) {
        this.setState({
            checkboxStyleObjectState: styleObject,
        });
    }
    changeClassNameState(className) {
        if (this.state.checkBoxclassNameState === className) {
            return;
        }
        this.setState({
            checkBoxclassNameState: className,
        });
    }
    changeComponentState(value, readOnly, visible) {
        this.changeValue(value);
        this.changeReadOnlyStatus(readOnly);
        this.changeVisibleStatus(visible);
    }
    render() {
        return (react_1.default.createElement("div", { className: this.state.checkBoxclassNameState }, this.state.checkBoxVisibleState && (react_1.default.createElement(checkbox_1.Checkbox, { id: this.props.symbolId, inputId: "binary", style: this.state.checkboxStyleObjectState, checked: this.state.checkBoxstatus, disabled: this.props.readOnly, onChange: (e) => this.updateValue(e.checked) }))));
    }
}
exports.default = CheckBox;
