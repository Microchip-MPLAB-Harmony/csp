import {
  nonSecureCallableColor,
  nonSecureColor,
  secureColor,
} from '../MainView/TrustZoneMainView';

import {
  GetBoxBottomHeight,
  GetBoxTopHeight,
  GetBoxWithText,
  GetSlider,
  sliderWidth,
} from './Memory';

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
        {
          //Adding slider
          GetSlider(
            parentSliderTopText,
            parentSliderBottomText,
            parentSliderValue,
            parentSliderMin,
            parentSliderMax,
            parentSliderHeight,
            parentUpdateSliderValue
          )
        }
      </div>
      <div>
        <div className="flex flex-column ">
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
            {
              // Adding Box
              GetBoxWithText(
                'flex flex-row',
                box3Text,
                nonSecureColor,
                GetBoxBottomHeight(
                  parentSliderValue,
                  parentSliderMax,
                  parentSliderHeight
                ),
                box3HexText,
                parentSliderValue !== parentSliderMin
              )
            }
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
    <div className="flex flex-row border-bottom-2">
      <div>
        {GetSlider(
          sliderTopText,
          sliderBottomText,
          sliderValue,
          sliderMin,
          sliderMax,
          sliderHeight,
          updateSliderValue
        )}
      </div>
      <div>
        <div className="flex flex-column">
          <div>
            {
              // Adding Box
              GetBoxWithText(
                sliderValue !== sliderMax && sliderValue !== sliderMin
                  ? 'flex flex-row border-bottom-2'
                  : 'flex flex-row',
                box1Text,
                secureColor,
                GetBoxTopHeight(sliderValue, sliderMax, sliderHeight),
                box1HexText,
                sliderValue !== sliderMax
              )
            }
          </div>
          <div>
            {
              // Adding Box
              GetBoxWithText(
                'flex flex-row',
                box2Text,
                nonSecureCallableColor,
                GetBoxBottomHeight(sliderValue, sliderMax, sliderHeight),
                box2HexText,
                sliderValue !== sliderMin
              )
            }
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
      <div className="flex flex-row border-y-2">
        <div>
          {GetSlider(
            'BS',
            'BNSC',
            slider1Value,
            slider1Min,
            slider1Max,
            slider1Height,
            updateSlider1Value
          )}
        </div>
        <div style={{ paddingLeft: bootPadding + 'px' }}>
          <div className="flex flex-column ">
            <div>
              {GetBoxWithText(
                slider1Value !== slider1Max && slider1Value !== slider1Min
                  ? 'flex flex-row border-bottom-2'
                  : 'flex flex-row',
                box1Text,
                secureColor,
                GetBoxTopHeight(slider1Value, slider1Max, slider1Height),
                box1HexText,
                slider1Value !== slider1Max
              )}
            </div>
            <div>
              {GetBoxWithText(
                'flex flex-row',
                box2Text,
                nonSecureCallableColor,
                GetBoxBottomHeight(slider1Value, slider1Max, slider1Height),
                box2HexText,
                slider1Value !== slider1Min
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
