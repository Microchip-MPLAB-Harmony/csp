import { Dropdown as PrimeDropDown } from "primereact/dropdown";
import React from "react";
import {
  UpdateSymbolValue,
  GetSymbolValue,
  AddSymbolListener,
} from "../SymbolAccess";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";
import { convertToBoolean } from "../Utils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  symbolValue: any;
  symbolArray: any;
  styleObject: any;
  className: any;
  readOnly: boolean;
  visible: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  comboSelectedValue?: any;
  comboReadOnlyStatue?: any;
  comboVisibleState?: any;
  comboStyleObjectState?: any;
  comboclassNameState?: any;
}
let obj: DropDown | null = null;
class DropDown extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      comboSelectedValue: GetSymbolValue(
        this.props.componentId,
        this.props.symbolId
      ),
      comboReadOnlyStatue: this.props.readOnly,
      comboVisibleState: this.props.visible,
      comboStyleObjectState: this.props.styleObject,
      comboclassNameState: this.props.className,
    };
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(event: { value: any }) {
    this.changeValue(event.value);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, event.value);
    this.props.onChange(event);
  }

  changeValue(value: any) {
    if (this.state.comboSelectedValue === value) {
      return;
    }
    this.setState({
      comboSelectedValue: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.comboReadOnlyStatue === value) {
      return;
    }
    this.setState({
      comboReadOnlyStatue: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.comboVisibleState === value) {
      return;
    }
    this.setState({
      comboVisibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      comboStyleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.comboclassNameState === className) {
      return;
    }
    this.setState({
      comboclassNameState: className,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(editable);
    this.changeVisibleStatus(visible);
  }

  render() {
    return (
      <div>
        <div className={this.state.comboclassNameState}>
          {this.state.comboVisibleState && (
            <PrimeDropDown
              id={this.props.symbolId}
              style={this.state.comboStyleObjectState}
              value={this.state.comboSelectedValue}
              options={this.props.symbolArray}
              disabled={this.state.comboReadOnlyStatue}
              onChange={(e) => this.updateValue(e)}
            />
          )}
        </div>
      </div>
    );
  }
}
export default DropDown;
