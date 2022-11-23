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

import { useEffect, useState } from 'react';
import {
  AddSymbolListener,
  SetComponentId,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

import { DMAChannel } from '../service/DMAChannel';
import { dmaService } from '../service/DMAService';

export default function ChannelsViewModel() {
  const [channels, setChannels] = useState<DMAChannel[]>([]);

  useEffect(() => {
    SetComponentId('core');

    setChannels(dmaService.allChannels());

    registerAllChannelEnableSymbols();
  }, []);

  const registerAllChannelEnableSymbols = () => {
    dmaService
      .allChannels()
      .map((channel) => channel.triggerSourceLockSymbolID)
      .forEach((symbolID: any) => {
        globalSymbolSStateData.set(symbolID, { changeValue: refetchChannels });
        AddSymbolListener(symbolID);
      });
  };

  const refetchChannels = (value: any) => {
    setChannels(dmaService.allChannels());
  };

  const setChannelEnable = (dmaChannel: DMAChannel, enable: boolean) => {
    if (!enable) dmaService.resetChannel(dmaChannel);

    const newChannels = channels.map((channel) => {
      if (channel.channelNumber === dmaChannel.channelNumber) {
        channel.enabled = enable;
      }
      return channel;
    });

    setChannels(newChannels);
  };

  const setChannelLock = (dmaChannel: DMAChannel, locked: boolean) => {
    const newChannels = channels.map((channel) => {
      if (channel.channelNumber === dmaChannel.channelNumber) {
        channel.locked = locked;
      }
      return channel;
    });

    setChannels(newChannels);
  };

  return {
    channels,
    setChannelEnable,
  };
}
