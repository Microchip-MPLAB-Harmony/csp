import { nonSecureCallableColor, nonSecureColor, secureColor } from '../MainView/TrustZoneMainView';
import GetBoxWithText from './GetBoxWithText';
import GetSlider from './GetSlider';

import { GetBoxBottomHeight, GetBoxTopHeight, sliderWidth } from './Memory';

export function GetBSOrASDiv(
  customClassName: string,
  parentSliderTopText: string,
  parentSliderBottomText: string,
  sliderTopText: string,
  sliderBottomText: string,
  parentSliderValue: any,
  parentSliderMin: any,
  parentSliderMax: any,
  parentSliderHeight: any,
  parentUpdateSliderValue: any,
  sliderValue: any,
  sliderMin: any,
  sliderMax: any,
  sliderHeight: any,
  updateSliderValue: any,
  box1Text: any,
  box1HexText: any,
  box2Text: any,
  box2HexText: any,
  box3Text: any,
  box3HexText: any,
  sliderBoxViewStatus: boolean,
  nonSecureBoxPaddingLeft: any
) {
  if (!sliderBoxViewStatus) {
    return;
  }
  return (
    <div className={customClassName}>
      <div style={{ paddingRight: sliderWidth }}>
        <GetSlider
          sliderTopText={parentSliderTopText}
          sliderBottomText={parentSliderBottomText}
          sliderValue={parentSliderValue}
          sliderMin={parentSliderMin}
          sliderMax={parentSliderMax}
          sliderHeight={parentSliderHeight}
          updateSliderValue={parentUpdateSliderValue}
        />
      </div>
      <div>
        <div className='flex flex-column '>
          <div>
            {GetBNSCOrANSCDiv(
              sliderTopText,
              sliderBottomText,
              sliderValue,
              sliderMin,
              sliderMax,
              sliderHeight,
              updateSliderValue,
              box1Text,
              box1HexText,
              box2Text,
              box2HexText,
              parentSliderValue !== parentSliderMax
            )}
          </div>
          <div style={{ paddingLeft: nonSecureBoxPaddingLeft + 'px' }}>
            <GetBoxWithText
              classCustom={'flex flex-row'}
              displayText={box3Text}
              color={nonSecureColor}
              boxHeight={GetBoxBottomHeight(parentSliderValue, parentSliderMax, parentSliderHeight)}
              hexDisplayText={box3HexText}
              textDisplayStatus={parentSliderValue !== parentSliderMin}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export function GetBNSCOrANSCDiv(
  sliderTopText: string,
  sliderBottomText: string,
  sliderValue: any,
  sliderMin: any,
  sliderMax: any,
  sliderHeight: any,
  updateSliderValue: any,
  box1Text: any,
  box1HexText: any,
  box2Text: any,
  box2HexText: any,
  sliderBoxViewStatus: boolean
) {
  if (!sliderBoxViewStatus) {
    return;
  }
  return (
    <div className='flex flex-row border-bottom-2'>
      <div>
        <GetSlider
          sliderTopText={sliderTopText}
          sliderBottomText={sliderBottomText}
          sliderValue={sliderValue}
          sliderMin={sliderMin}
          sliderMax={sliderMax}
          sliderHeight={sliderHeight}
          updateSliderValue={updateSliderValue}
        />
      </div>
      <div>
        <div className='flex flex-column'>
          <div>
            <GetBoxWithText
              classCustom={
                sliderValue !== sliderMax && sliderValue !== sliderMin
                  ? 'flex flex-row border-bottom-2'
                  : 'flex flex-row'
              }
              displayText={box1Text}
              color={secureColor}
              boxHeight={GetBoxTopHeight(sliderValue, sliderMax, sliderHeight)}
              hexDisplayText={box1HexText}
              textDisplayStatus={sliderValue !== sliderMax}
            />
          </div>
          <div>
            <GetBoxWithText
              classCustom={'flex flex-row'}
              displayText={box2Text}
              color={nonSecureCallableColor}
              boxHeight={GetBoxBottomHeight(sliderValue, sliderMax, sliderHeight)}
              hexDisplayText={box2HexText}
              textDisplayStatus={sliderValue !== sliderMin}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export function GetBootRegion(
  slider1Value: any,
  slider1Min: any,
  slider1Max: any,
  slider1Height: any,
  updateSlider1Value: any,
  box1Text: any,
  box1HexText: any,
  box2Text: any,
  box2HexText: any,
  bootPadding: any
) {
  return (
    <div>
      <div className='flex flex-row border-y-2'>
        <div>
          <GetSlider
            sliderTopText={'BS'}
            sliderBottomText={'BNSC'}
            sliderValue={slider1Value}
            sliderMin={slider1Min}
            sliderMax={slider1Max}
            sliderHeight={slider1Height}
            updateSliderValue={updateSlider1Value}
          />
        </div>
        <div style={{ paddingLeft: bootPadding + 'px' }}>
          <div className='flex flex-column '>
            <div>
              <GetBoxWithText
                classCustom={
                  slider1Value !== slider1Max && slider1Value !== slider1Min
                    ? 'flex flex-row border-bottom-2'
                    : 'flex flex-row'
                }
                displayText={box1Text}
                color={secureColor}
                boxHeight={GetBoxTopHeight(slider1Value, slider1Max, slider1Height)}
                hexDisplayText={box1HexText}
                textDisplayStatus={slider1Value !== slider1Max}
              />
            </div>
            <div>
              <GetBoxWithText
                classCustom={'flex flex-row'}
                displayText={box2Text}
                color={nonSecureCallableColor}
                boxHeight={GetBoxBottomHeight(slider1Value, slider1Max, slider1Height)}
                hexDisplayText={box2HexText}
                textDisplayStatus={slider1Value !== slider1Min}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
