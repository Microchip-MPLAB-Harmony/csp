import { InputText as PrimeInputText } from "primereact/inputtext";
import React from "react";
import {
  AddSymbolListener,
  GetSymbolValue,
  UpdateSymbolValue,
} from "../SymbolAccess";
import { convertToBoolean } from "../Utils";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  component_id: string;
  symbolId: string;
  symbolListeners: any;
  styleObject: any;
  className: any;
  onChange: (arg0: any) => void;
  readOnly: boolean;
  visible: boolean;
}

interface IState {
  inputTextSelectedValue?: any;
  inputTextReadOnlyState?: boolean;
  inputTextVisibleState?: boolean;
  inputTextStyleObjectState?: any;
  inputTextclassNameState?: any;
}
let obj: InputText | null = null;

class InputText extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      inputTextSelectedValue: GetSymbolValue(
        this.props.component_id,
        this.props.symbolId
      ),
      inputTextReadOnlyState: this.props.readOnly,
      inputTextVisibleState: this.props.visible,
      inputTextStyleObjectState: this.props.styleObject,
      inputTextclassNameState: this.props.className,
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
    UpdateSymbolValue(
      this.props.component_id,
      this.props.symbolId,
      event.value
    );
    this.props.onChange(event);
  }

  changeValue(value: any) {
    if (this.state.inputTextSelectedValue === value) {
      return;
    }
    this.setState({
      inputTextSelectedValue: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.inputTextReadOnlyState === value) {
      return;
    }
    this.setState({
      inputTextReadOnlyState: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.inputTextVisibleState === value) {
      return;
    }
    this.setState({
      inputTextVisibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      inputTextStyleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.inputTextclassNameState === className) {
      return;
    }
    this.setState({
      inputTextclassNameState: className,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(editable);
    this.changeVisibleStatus(visible);
  }

  render() {
    return (
      <div className={this.state.inputTextclassNameState}>
        {this.state.inputTextVisibleState && (
          <PrimeInputText
            id={this.props.symbolId}
            style={this.state.inputTextStyleObjectState}
            tooltip={this.state.inputTextSelectedValue}
            value={this.state.inputTextSelectedValue}
            disabled={this.state.inputTextReadOnlyState}
            onChange={(e) => this.updateValue(e.target)}
          />
        )}
      </div>
    );
  }
}
export default InputText;
