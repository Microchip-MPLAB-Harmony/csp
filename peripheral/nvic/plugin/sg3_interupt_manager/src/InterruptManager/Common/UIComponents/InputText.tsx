import { InputText } from "primereact/inputtext";
import React from "react";
import {
  AddSymbolListner,
  GetSymbolValue,
  UpdateSymbolValue,
} from "../SymbolAccess";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  component_id: string;
  symbolId: string;
  width: string;
  onChange: (arg0: any) => void;
  editable: boolean;
}

interface IState {
  inputTextSelectedValue?: any;
}

class GetInputText extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      inputTextSelectedValue: GetSymbolValue(
        this.props.component_id,
        this.props.symbolId
      ),
    };
    globalSymbolSStateData.set(props.symbolId, this);
    AddSymbolListner(props.symbolId);
  }

  updateValue(event: { value: any }) {
    UpdateSymbolValue(
      this.props.component_id,
      this.props.symbolId,
      event.value
    );
    this.props.onChange(event);
    this.changeValue(event.value);
  }

  changeValue(value: any) {
    this.setState({
      inputTextSelectedValue: value,
    });
  }

  render() {
    return (
      <div>
        <InputText
          id={this.props.symbolId}
          style={{ width: this.props.width }}
          tooltip={this.state.inputTextSelectedValue}
          value={this.state.inputTextSelectedValue}
          disabled={!this.props.editable}
          onChange={(e) => this.updateValue(e.target)}
        />
      </div>
    );
  }
}
export default GetInputText;
