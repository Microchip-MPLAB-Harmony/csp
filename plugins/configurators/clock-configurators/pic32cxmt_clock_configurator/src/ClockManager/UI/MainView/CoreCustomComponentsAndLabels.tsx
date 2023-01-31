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
import { component_id } from './MainBlock';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { AddPrefixDivSymbolLabel } from 'clock-common/lib/ClockUtils/ClockLabelUtils';
import { AddCheckBox } from 'clock-common/lib/ClockUtils/ClockCommonUtils';
import ProcessorClockControllerBLCSS from './ProcessorClockControllerBoldLabel/ProcessorClockControllerBLCSS';
import ProcessorClockControllerBLCPCSS from './ProcessorClockControllerBoldLabel/ProcessorClockControllerBLCPCSS';

export function AddCoreCustomLabels() {
  try {
    return (
      <div>
        {AddPrefixDivSymbolLabel(
          'label_core0PresValue',
          component_id,
          'CLK_CPU_CKR_PRES',
          GetDiVAddedText
        )}
        {AddPrefixDivSymbolLabel(
          'label_core1CPPRES',
          component_id,
          'CLK_CPU_CKR_CPPRES',
          GetDiVAddedText
        )}

        {/* Core 0 symbols*/}

        {AddCheckBox(
          component_id,
          'CLK_CPU_CKR_RATIO_MCK0DIV',
          'CLK_CPU_CKR_RATIO_MCK0DIV'
        )}
        {AddPrefixDivSymbolLabel(
          'label_core0MCK0DIVValue',
          component_id,
          'CLK_CPU_CKR_RATIO_MCK0DIV',
          GetCoreLabel
        )}
        {AddCheckBox(
          component_id,
          'CLK_CPU_CKR_RATIO_MCK0DIV2',
          'CLK_CPU_CKR_RATIO_MCK0DIV2'
        )}
        {AddPrefixDivSymbolLabel(
          'label_core0MCK0DIV2Value',
          component_id,
          'CLK_CPU_CKR_RATIO_MCK0DIV2',
          GetCoreLabel
        )}

        <ProcessorClockControllerBLCSS symboListenerValue={'CLK_CPU_CKR_CSS'} />

        {/* Core 1 symbols*/}

        <ProcessorClockControllerBLCPCSS
          symboListenerValue={'CLK_CPU_CKR_CPCSS'}
        />

        {AddCheckBox(
          component_id,
          'CLK_CPU_CKR_RATIO_MCK1DIV',
          'CLK_CPU_CKR_RATIO_MCK1DIV'
        )}
        {AddPrefixDivSymbolLabel(
          'label_core1MCK1Div',
          component_id,
          'CLK_CPU_CKR_RATIO_MCK1DIV',
          GetCoreLabel
        )}
      </div>
    );
  } catch (err) {}
}

function GetDiVAddedText(text: any) {
  try {
    let divValue = RemoveDiv(text);
    divValue = divValue.replace('CLK', '');
    divValue = divValue.replace('DIV', '');
    return '/ ' + divValue;
  } catch (err) {}
}

function RemoveDiv(value: string) {
  let newValue = value.split('_');
  if (newValue.length === 0) {
    return newValue[0];
  }
  return newValue[1];
}

function GetCoreLabel(checkBoxStatus: any) {
  let labelValue = '1';
  if (convertToBoolean(checkBoxStatus)) {
    labelValue = '2';
  }
  return '/ ' + labelValue;
}
