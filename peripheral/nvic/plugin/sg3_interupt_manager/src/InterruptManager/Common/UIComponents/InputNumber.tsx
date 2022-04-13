import { InputNumber } from "primereact/inputnumber";
import React from "react";
import { AddSymbolListner, UpdateSymbolValue } from "../SymbolAccess";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolValue: any;
  minFractionValue: any;
  minValue: any;
  maxValue: any;
  styleObject: any;
  editable: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  inputNumberSelectedValue?: any;
}

class GetInputNumber extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);

    this.state = {
      inputNumberSelectedValue: this.props.symbolValue,
    };
    globalSymbolSStateData.set(props.symbolId, this);
    AddSymbolListner(props.symbolId);
  }

  updateValue(value: any) {
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, value);
    this.props.onChange(value);
    this.changeValue(value);
  }

  changeValue(value: any) {
    this.setState({
      inputNumberSelectedValue: value,
    });
  }

  render() {
    return (
      <div>
        <InputNumber
          id={this.props.symbolId}
          style={this.props.styleObject}
          value={this.state.inputNumberSelectedValue}
          minFractionDigits={this.props.minFractionValue}
          maxFractionDigits={8}
          mode="decimal"
          showButtons
          min={this.props.minValue}
          max={this.props.maxValue}
          disabled={!this.props.editable}
          onChange={(target) => this.updateValue(target.value)}
        />
      </div>
    );
  }
}
export default GetInputNumber;
