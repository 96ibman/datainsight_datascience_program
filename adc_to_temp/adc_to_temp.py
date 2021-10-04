#!/usr/bin/env python
# coding: utf-8

# In[1]:


SYSVOLT = 5
ADC_RESOLUTION = 4095
MAX_VOLT = 2.442
MIN_VOLT = 0

MIN_TEMP = -50
MAX_TEMP = 50


# In[2]:


def adc_raw_value(v):
    if(v >= MIN_VOLT and v <= MAX_VOLT):
        ADC = (v*(ADC_RESOLUTION/SYSVOLT))
        return round(ADC)
    else:
        return None


# In[3]:


def adc_to_c(x):
    if x == 0:
        return -50
    else:
        return ((adc_to_c(x-1)) + 0.05)


# In[4]:


def sensor_temp(v):
    print(f"SENSOR READ: {v} Volt")
    ADC = adc_raw_value(v)
    if ADC is None:
        print("Voltage is not within the sensor range")
    else:
        print("**********************\nAnalog to Digital Convertion\n**********************")
        print(f"Analog: {v}\nDigital: {ADC}")
        print("**********************")
        print(f"Temprature is: {round(adc_to_c(ADC))}")


# In[5]:


sensor_temp(MIN_VOLT)


# In[6]:


sensor_temp(MAX_VOLT) 


# In[7]:


sensor_temp(1.221) 


# In[8]:


sensor_temp(1.5)

