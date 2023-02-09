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
import { DMAChannel } from './DMAChannel';
import _ from 'lodash';

import { pluginService } from './PluginService';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { error } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import { clearAllSymbols } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';

export const COMPONENT_ID = 'core';

export class DMAService {
  private readonly TOTAL_CHANNELS: number;
  constructor() {
    this.TOTAL_CHANNELS = GetSymbolValue(
      COMPONENT_ID,
      pluginService.symbolConfig.totalChannelsCount
    );
  }

  createDMAChannel = (channelNumber: number) => {
    if (channelNumber >= this.totalChannels || channelNumber < 0) {
      error(
        'DMA Manager : ' +
          'Unable to create DMA channel instance : ' +
          channelNumber +
          ', Allowed Channel numbers from 0 to ' +
          (this.totalChannels - 1)
      );
      return undefined;
    }

    const dmaChannel = new DMAChannel(channelNumber);
    dmaChannel.enabled = this.isChannelActive(dmaChannel);
    dmaChannel.locked = this.isChannelLocked(dmaChannel);

    return dmaChannel;
  };

  get totalChannels() {
    return this.TOTAL_CHANNELS;
  }

  isChannelWithinRange(channelNumber: number) {
    return channelNumber < this.TOTAL_CHANNELS && channelNumber >= 0;
  }

  allChannels = (): DMAChannel[] => {
    return _.range(this.TOTAL_CHANNELS).map(this.createDMAChannel);
  };

  isChannelActive(dmaChannel: DMAChannel): boolean {
    return (
      GetSymbolValue(COMPONENT_ID, dmaChannel.enableChannelSymbolID) === 'true'
    );
  }

  isChannelLocked(dmaChannel: DMAChannel): boolean {
    return (
      GetSymbolValue(COMPONENT_ID, dmaChannel.triggerSourceLockSymbolID) ===
      'true'
    );
  }

  resetChannel = (dmaChannel: DMAChannel) => {
    clearAllSymbols(COMPONENT_ID, [
      dmaChannel.enableChannelSymbolID,
      dmaChannel.enableInterruptSymbolID,
      dmaChannel.triggerSourceSymbolID,
      dmaChannel.prioritySymbolID,
    ]);
  };
}

export const dmaService = new DMAService();
