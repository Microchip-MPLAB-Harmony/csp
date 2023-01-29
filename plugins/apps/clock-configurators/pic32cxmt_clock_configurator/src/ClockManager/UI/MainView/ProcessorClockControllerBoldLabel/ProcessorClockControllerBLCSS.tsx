/*
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
 */
import { StateLabelInterface } from '@mplab_harmony/harmony-plugin-ui/build/componentInterfaces/StateLabelInterface';
import React from 'react';
import { RegisterLabelSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/global/Data';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { component_id } from '../MainBlock';
import { AddSymboLabelWithSuffixWithBold } from 'clock-common/lib/ClockUtils/ClockLabelUtils';
import { CompareStrings } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';

interface IProps {
  symboListenerValue: any;
}
interface IState {
  listenSymbolValueState: any;
}
class ProcessorClockControllerBoldLabelsCSS
  extends React.Component<IProps, IState>
  implements StateLabelInterface
{
  constructor(props: IProps) {
    super(props);
    this.componentWillReceiveProps(props);
    RegisterLabelSymbolSStateData(props.symboListenerValue, this);
  }

  changeLabelState(newValue: any): void {
    throw new Error('Method not implemented.');
  }
  changeLabelStyleState(styleObject: any): void {
    throw new Error('Method not implemented.');
  }
  changeLabelVisibleStatus(visibilitySttus: any): void {
    throw new Error('Method not implemented.');
  }
  changeLabelClassNameState(classNameObject: any): void {
    throw new Error('Method not implemented.');
  }
  labelLinkedSymbolChanged(symbolid: any, value: any): void {
    this.setState({
      listenSymbolValueState: value,
    });
  }

  componentWillReceiveProps(props: IProps) {
    this.state = {
      listenSymbolValueState: GetSymbolValue(
        component_id,
        this.props.symboListenerValue
      ),
    };
  }

  render() {
    return (
      <div className="card">
        {AddSymboLabelWithSuffixWithBold(
          'label_core0MdclockFreq',
          component_id,
          'MD_SLOW_CLK_FREQUENCY',
          ' Hz',
          CompareStrings(this.state.listenSymbolValueState, 'MD_SLOW_CLK')
        )}
        {AddSymboLabelWithSuffixWithBold(
          'label_core0MainClkFrequency',
          component_id,
          'MAINCK_FREQUENCY',
          ' Hz',
          CompareStrings(this.state.listenSymbolValueState, 'MAINCK')
        )}
        {AddSymboLabelWithSuffixWithBold(
          'label_core0PLLACK1',
          component_id,
          'PLLACK1_FREQUENCY',
          ' Hz',
          CompareStrings(this.state.listenSymbolValueState, 'PLLACK1')
        )}
        {AddSymboLabelWithSuffixWithBold(
          'label_core0PLLBCK',
          component_id,
          'PLLBCK_FREQUENCY',
          ' Hz',
          CompareStrings(this.state.listenSymbolValueState, 'PLLBCK')
        )}
      </div>
    );
  }
}

export default ProcessorClockControllerBoldLabelsCSS;
