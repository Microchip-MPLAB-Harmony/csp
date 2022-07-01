import { InputNumber as PrimeInputNumber} from "primereact/inputnumber";
import React from "react";
import { AddSymbolListener, UpdateSymbolValue } from "../SymbolAccess";
import { convertToBoolean } from "../Utils";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  symbolValue: any;
  minFractionValue: any;
  minValue: any;
  maxValue: any;
  styleObject: any;
  className: any;
  readOnly: boolean;
  visible: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  inputNumberSelectedValue?: any;
  inputNumberReadOnlyStatue?: any;
  inputNumberVisibleState?: any;
  inputNumberStyleObjectState?: any;
  inputNumberclassNameState?: any;
}
let obj: InputNumber | null = null;
class InputNumber extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);

    this.state = {
      inputNumberSelectedValue: this.props.symbolValue,
      inputNumberReadOnlyStatue: this.props.readOnly,
      inputNumberVisibleState: this.props.visible,
      inputNumberStyleObjectState: this.props.styleObject,
      inputNumberclassNameState: this.props.className,
    };
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(value: any) {
    this.changeValue(value);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, value);
    this.props.onChange(value);
  }

  changeValue(value: any) {
    if (this.state.inputNumberSelectedValue === value) {
      return;
    }
    this.setState({
      inputNumberSelectedValue: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.inputNumberReadOnlyStatue === value) {
      return;
    }
    this.setState({
      inputNumberReadOnlyStatue: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.inputNumberVisibleState === value) {
      return;
    }
    this.setState({
      inputNumberVisibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      inputNumberStyleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.inputNumberclassNameState === className) {
      return;
    }
    this.setState({
      inputNumberclassNameState: className,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(editable);
    this.changeVisibleStatus(visible);
  }

  render() {
    return (
      <div className={this.state.inputNumberclassNameState}>
        {this.state.inputNumberVisibleState && (
          <PrimeInputNumber
            id={this.props.symbolId}
            style={this.state.inputNumberStyleObjectState}
            value={this.state.inputNumberSelectedValue}
            minFractionDigits={this.props.minFractionValue}
            maxFractionDigits={8}
            mode="decimal"
            showButtons
            min={this.props.minValue}
            max={this.props.maxValue}
            disabled={this.state.inputNumberReadOnlyStatue}
            onValueChange={(target) => this.updateValue(target.value)}
          />
        )}
      </div>
    );
  }
}
export default InputNumber;
