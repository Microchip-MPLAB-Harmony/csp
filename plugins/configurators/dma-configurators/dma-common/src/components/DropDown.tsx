/*******************************************************************************
 * Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software
 * and any derivatives exclusively with Microchip products. It is your
 * responsibility to comply with third party license terms applicable to your
 * use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
 * PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
 * ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *******************************************************************************/
import {
  AddSymbolListener,
  GetSymbolValue,
  UpdateSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { Dropdown as PrimeDropDown } from 'primereact/dropdown';
import React from 'react';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  symbolValue: any;
  symbolArray: any;
  styleObject?: any;
  className?: any;
  readOnly: boolean;
  visible: boolean;
  beforeChange?: () => void;
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
    this.componentWillReceiveProps(props);
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  componentWillReceiveProps(props: IProps) {
    this.state = {
      comboSelectedValue: GetSymbolValue(props.componentId, props.symbolId),
      comboReadOnlyStatue: props.readOnly,
      comboVisibleState: props.visible,
      comboStyleObjectState: props.styleObject,
      comboclassNameState: props.className,
    };
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(event: { value: any }) {
    this.props.beforeChange?.();
    this.changeValue(event.value);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, event.value);
    this.props.onChange(event);
  }

  changeValue(value: any) {
    if (this.state.comboSelectedValue === value) {
      return;
    }
    this.props.onChange(value);
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
              disabled={this.props.readOnly}
              onChange={(e) => this.updateValue(e)}
            />
          )}
        </div>
      </div>
    );
  }
}
export default DropDown;
