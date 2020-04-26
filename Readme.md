## Inspiration

The most effective way to contain the pandemic is to trace it, mitigate and contain it. As such, there is no current app / solution to assess the risk of being infected by visiting a place such as supermarket or park, prior to the actual visit. 

## What it does

Traceable collects user’s medical conditions, personal symptoms, nature of work, family connections as well as contact tracing to evaluate a personal risk score. Users can log their intention to visit different places like supermarket, park, bank, etc on a specific date & time, the user can check the live risk associated with the intended location at the time and date of visit. These location risk levels are predicted based on the risk scores of the individuals who have logged their intention to visit, as well as accumulated risk from the past visits who had, or later developed symptoms.

## How we built it

The app's backend is built on Python, including the dashboard to visualise the risk levels at different locations, at different times. The front end has been prototyped in proto.io. Going ahead, the app's frontend will be built on flutter. 

## Challenges we ran into

With the little time we had, and no prior collected data for the app's data model to be developed and validated, we had to reverse engineering the problem, using synthetic data. Developing the logic of calculating the various risk levels for individuals and locations, and interconnecting them were also challenging.

## Accomplishments that we're proud of

A prototyped idea with a running data-model and a well thought-out logic, as well as a inter-connected backend dashboard.

## What we learned

We learned to develop a logic and data-model without actual data. We also learned that we would require more resources, wider technical skillset as well as domain knowledge / input to validate our assumptions and logic.

## What's next for Traceable

1) To develop fully functional app, with support from partners, government bodies
2) To deploy the app locally, initially in order to validate the app and the associated risk levels
3) To engage with users to improve the user experience and add valuable features
4) This app should intended to be released by a government body, for sole purpose of mitigating the current and future pandemic, and to support medical research