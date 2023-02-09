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
import { Divider } from 'primereact/divider';
import useViewModel from '../active-channel-table/ChannelsViewModel';

import { pluginService } from '../service/PluginService';

import './channel-setting.css';
import { useBetween } from 'use-between';
import { dmaService } from '../service/DMAService';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import {
  GetSymbolReadOnlyStatus,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import AddMultipleUIComponentsWithLabel from 'dma-common/lib/utils/AddMultipleUIComponentsWithLabel';

const component_id = 'core';

function parentUpdateCallBack() {}

const ChannelSetting = () => {
  const { currentChannelNumber } = useBetween(useViewModel);

  const isCurrentChannelEnabled = () => {
    dmaService.isChannelActive(currentChannelNumber);
  };

  const settingSymbols = pluginService.symbolConfig.settings;
  const linkedListMode = pluginService.symbolConfig.linkedListMode;

  return (
    <section className="channel-setting">
      <div className="flex">
        <CheckBox
          componentId={component_id}
          symbolId={linkedListMode}
          symbolValue={GetSymbolValue(component_id, linkedListMode)}
          readOnly={GetSymbolReadOnlyStatus(component_id, linkedListMode)}
          symbolListeners={[linkedListMode]}
          visible={true}
          styleObject={undefined}
          className={undefined}
          onChange={function (arg0: any): void {
            throw new Error('Function not implemented.');
          }}
        />
        <label
          htmlFor="binary"
          className="p-checkbox-label"
          style={{ marginLeft: '10px' }}
        >
          Use Linked List Mode
        </label>
      </div>
      <Divider layout="horizontal" />
      {dmaService.isChannelActive(currentChannelNumber) ? (
        <div className="flex flex-column">
          <h2 className="channel-setting-title">
            DMA Channel {currentChannelNumber} Settings
          </h2>
          <div className=" mt-5">
            <AddMultipleUIComponentsWithLabel
              componentId={component_id}
              parentUpdate={parentUpdateCallBack}
              symbolsArray={settingSymbols.map((e) =>
                e.replace(
                  '{DMA_CHANNEL_NUMBER}',
                  currentChannelNumber.toString()
                )
              )}
            />
          </div>
        </div>
      ) : (
        <h4>Please select any DMA Channel to configure!</h4>
      )}
    </section>
  );
};

export default ChannelSetting;
