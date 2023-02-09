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
  UpdateSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { Checkbox as PrimeCheckBox } from 'primereact/checkbox';
import React from 'react';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  symbolValue: string;
  styleObject?: any;
  className?: any;
  readOnly: boolean;
  visible: boolean;
  beforeChange?: () => void;
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
    this.componentWillReceiveProps(props);
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  componentWillReceiveProps(props: IProps) {
    this.state = {
      checkBoxstatus: convertToBoolean(props.symbolValue),
      checkBoxReadOnlyState: props.readOnly,
      checkBoxVisibleState: props.visible,
      checkboxStyleObjectState: props.styleObject,
      checkBoxclassNameState: props.className,
    };
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(checked: boolean) {
    this.props.beforeChange?.();
    this.changeValue(checked);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, checked);
    this.props.onChange(checked);
  }

  changeValue(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxstatus === value) {
      return;
    }
    this.props.onChange(value);
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
            disabled={this.props.readOnly}
            onChange={(e) => this.updateValue(e.checked)}
          />
        )}
      </div>
    );
  }
}
export default CheckBox;
