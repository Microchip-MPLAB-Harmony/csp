import { Checkbox as PrimeCheckBox } from "primereact/checkbox";
import React from "react";
import { AddSymbolListener, UpdateSymbolValue } from "../SymbolAccess";
import { convertToBoolean } from "../Utils";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  symbolValue: string;
  styleObject: any;
  className: any;
  readOnly: boolean;
  visible: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  checkBoxstatus?: any;
  checkBoxReadOnlyState?: boolean;
  checkBoxVisibleState?: boolean;
  checkboxStyleObjectState?: any;
  checkBoxclassNameState?: any;
}
let obj: CheckBox | null = null;

class CheckBox extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      checkBoxstatus: convertToBoolean(this.props.symbolValue),
      checkBoxReadOnlyState: this.props.readOnly,
      checkBoxVisibleState: this.props.visible,
      checkboxStyleObjectState: this.props.styleObject,
      checkBoxclassNameState: this.props.className,
    };
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(checked: boolean) {
    this.changeValue(checked);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, checked);
    this.props.onChange(checked);
  }

  changeValue(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxstatus === value) {
      return;
    }
    this.setState({
      checkBoxstatus: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxReadOnlyState === value) {
      return;
    }
    this.setState({
      checkBoxReadOnlyState: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxVisibleState === value) {
      return;
    }
    this.setState({
      checkBoxVisibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      checkboxStyleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.checkBoxclassNameState === className) {
      return;
    }
    this.setState({
      checkBoxclassNameState: className,
    });
  }

  changeComponentState(value: any, readOnly: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(readOnly);
    this.changeVisibleStatus(visible);
  }

  render() {
    return (
      <div className={this.state.checkBoxclassNameState}>
        {this.state.checkBoxVisibleState && (
          <PrimeCheckBox
            id={this.props.symbolId}
            inputId="binary"
            style={this.state.checkboxStyleObjectState}
            checked={this.state.checkBoxstatus}
            disabled={this.state.checkBoxReadOnlyState}
            onChange={(e) => this.updateValue(e.checked)}
          />
        )}
      </div>
    );
  }
}
export default CheckBox;
