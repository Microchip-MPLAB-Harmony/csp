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
import { pluginService } from './PluginService';

export class DMAChannel {
  private readonly _channelName: string;
  private readonly _enableChannelSymbolID: string;
  private readonly _triggerSourceSymbolID: string;
  private readonly _triggerSourceLockSymbolID: string;
  private readonly _prioritySymbolID: string;
  private readonly _enableInterruptSymbolID: string;

  private _enabled = false;
  private _locked = false;

  constructor(private _channelNumber: number) {
    this._channelName = 'DMAC Channel ' + _channelNumber;

    const symbolConfig = pluginService.symbolConfig;
    this._enableChannelSymbolID = symbolConfig.enableChannel.replace(
      '{DMA_CHANNEL_NUMBER}',
      _channelNumber.toString()
    );

    this._triggerSourceSymbolID = symbolConfig.triggerSource.replace(
      '{DMA_CHANNEL_NUMBER}',
      _channelNumber.toString()
    );

    this._prioritySymbolID = symbolConfig.priority.replace(
      '{DMA_CHANNEL_NUMBER}',
      _channelNumber.toString()
    );

    this._enableInterruptSymbolID = symbolConfig.enableInterrupt.replace(
      '{DMA_CHANNEL_NUMBER}',
      _channelNumber.toString()
    );

    this._triggerSourceLockSymbolID = symbolConfig.triggerSourceLock.replace(
      '{DMA_CHANNEL_NUMBER}',
      _channelNumber.toString()
    );
  }

  get channelNumber() {
    return this._channelNumber;
  }

  get channelName() {
    return this._channelName;
  }

  get enableChannelSymbolID() {
    return this._enableChannelSymbolID;
  }

  get triggerSourceSymbolID() {
    return this._triggerSourceSymbolID;
  }

  get prioritySymbolID() {
    return this._prioritySymbolID;
  }

  get enableInterruptSymbolID() {
    return this._enableInterruptSymbolID;
  }

  get triggerSourceLockSymbolID() {
    return this._triggerSourceLockSymbolID;
  }

  set enabled(_enabled: boolean) {
    this._enabled = _enabled;
  }

  get enabled() {
    return this._enabled;
  }

  set locked(_locked: boolean) {
    this._locked = _locked;
  }

  get locked() {
    return this._locked;
  }
}
