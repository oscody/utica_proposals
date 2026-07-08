# Simple MVP Breakdown

Source: `UticaSS training meeting_July_02_2026_02-37-05_PM.md`

## What We Are Building

We need a simple online training website for Utica Security Training.

The MVP should let students:

- See the training programs.
- Pick a class day.
- Register and pay.
- Receive the live class meeting link.
- Attend the live class with camera on.
- Take a simple test.
- Receive a certificate only after the class is completed.

The main point is this: the training is live virtual training, not a prerecorded course library.

## MVP Features

### 1. Live Virtual Classes

Build the program around live classes using Zoom, Google Meet, Teams, or WebEx.

The instructor teaches live at a set time. Videos or materials can be used during the class, but the full training cannot be just prerecorded videos.

Proof:

- The meeting says the class is "live teaching" and "must be live" on lines 1662-1678.
- It says prerecorded-only training is not allowed and live teaching is required on lines 1680-1699.
- It confirms the program is "live virtual training" on lines 2466-2473.
- It says this is an instructor live at a set time on lines 2484-2492.

### 2. Simple Training Website

Build a separate training website or training section with the basic pages students need.

Minimum pages:

- Home
- About
- Programs / Courses
- Admissions / Enrollment
- Tuition / Pricing
- Contact
- FAQ

Proof:

- The meeting says to build a full website for the training school on lines 1317-1324.
- It lists homepage, about page, programs/courses, admissions, and tuition on lines 1389-1403.
- It repeats homepage, about, programs/courses, online classes, enrollment, and tuition/pricing on lines 2508-2516.
- It adds contact page and FAQ on lines 2619-2657.

### 3. Class Booking By Day

Students should book a class day, not a flexible time slot.

Example:

- Monday: 8-hour pre-assignment
- Tuesday: 16-hour OJT / second training day
- Wednesday or Thursday: annual in-service

The class time is fixed. For example, the class may start at 8 a.m. and end at 5 p.m., with breaks.

Proof:

- The meeting says the class is an 8-hour program with fixed timing on lines 1713-1744.
- It says students book by day, not by time, on lines 1761-1786.
- It gives examples of Monday for pre-assignment, Tuesday for OJT, and Wednesday/Thursday for in-service on lines 1791-1805.

### 4. Student Registration, Login, And Payment

Students need a way to enroll, pay once for the class, and access class details.

Payment can use Stripe or PayPal.

This is not a recurring subscription. Each class is a one-time payment. If students return next year for recertification, they pay again.

Proof:

- The meeting asks how payment will be handled on the site on lines 2526-2533.
- It names Stripe and PayPal as payment options on lines 2577-2587.
- It says payment is one-time and each class is one time on lines 2592-2611.
- It discusses student accounts/login and a dashboard on lines 2688-2701.
- It says students log in, do the assignment/test, and submit it on lines 2769-2791.

### 5. Meeting Link Delivery

After a student registers, the system should send them the class meeting URL or meeting code by email.

The class itself can happen on Google Meet, Zoom, Teams, or WebEx. The website does not have to host the video directly for MVP.

Proof:

- The meeting suggests generating a meeting code or URL and sending it to the student's email on lines 2121-2131.
- It says the class will connect through Google Meet and students will have access to the meeting ID on lines 2145-2155.

### 6. Attendance And Camera Rules

The MVP must track attendance.

For live virtual classes, students should be required to:

- Join at the correct time.
- Stay visible on camera.
- Not use a blank screen.
- Be counted in digital attendance.

This matters because certificates should only go to people who actually attended the class.

Proof:

- The meeting asks for digital attendance that can be submitted on lines 663-673.
- It says the team must make sure people do not get certificates without training on lines 1884-1904.
- It says students must log in at the same time, be on live camera, and cannot leave the camera blank on lines 2052-2071.
- It discusses monitoring cameras through Zoom or Google Meet on lines 2085-2104.

### 7. Recording And Storage

Classes need to be recorded and stored.

For MVP, the easiest path is to use the recording feature from Zoom, Google Meet, or Teams, then store recordings in a controlled storage location such as Google Drive.

Storage must be planned carefully because the meeting mentions keeping training records for two years.

Proof:

- The meeting says classes need to be recorded and mentions paid Zoom recording on lines 681-699.
- It says the website/platform needs the ability to record and store training, and mentions two-year storage on lines 2187-2206.
- It discusses Google Drive storage and buying more storage if needed on lines 2286-2329.

### 8. Certificate Process

Certificates should be generated only after the class is completed.

For MVP, use a certificate template with a signature. After confirming attendance and completion, the certificate can be emailed or made available for download.

Do not let students automatically receive certificates just because they logged in.

Proof:

- The meeting says certificates need to be created/generated for online training on lines 1821-1837.
- It says a certificate template can be generated for download after course completion on lines 1839-1862.
- It discusses adding a signature into the certificate process on lines 1878-1883.
- It says this is live training and the certificate should be generated after the session is completed on lines 1929-1966.

### 9. Simple Online Test

Add a simple multiple-choice test after the training.

For MVP, keep it basic:

- One test per class.
- Around 10 to 20 multiple-choice questions.
- Student submits the test online.
- Admin/instructor confirms completion before certificate release.

Proof:

- The meeting says tests are required on lines 2718-2749.
- It says online students need a dashboard/login to complete and submit work on lines 2760-2791.
- It says the test is one-time and multiple choice on lines 2811-2819.
- It estimates about 10 to 20 questions on lines 2820-2833.

### 10. Compliance And Admin Requirements

Add an admin compliance layer so the school can track the required DCJS live virtual training steps before, during, and after each class.

For MVP, the developer should build:

- Admin compliance checklist for DCJS approval readiness.
- Class announcement generator for the one-week advance DCJS email.
- Separate DCJS/auditor access link field for each class.
- Attendance roster with `COC` status for each student.
- Student ID verification fields: verified by video, verified by, timestamp, and notes.
- Required forms tracking for enrollment form, catalog, and student advisory notice.
- Locked, signed certificate PDF generation after completion approval.
- Recording archive with recording link, storage location, retention date, and share link.
- Prerecorded video usage tracker so clips do not replace live instruction.
- Acadis reporting helper reminding admin to enter `online training` after the instructor name and in the comment section.

These are platform features that support compliance. The actual emails, approvals, class monitoring, and final reporting are still admin/instructor responsibilities.

Proof:

- The procedures require the school to email a written virtual training request with platform, attendance, forms, and certificate procedures on `live_virtual_training_procedures.md` lines 14-24.
- The procedures require one-week advance online training announcements with course type, times, instructor, and audit link on `live_virtual_training_procedures.md` lines 30-34.
- The procedures require recordings to be retained for two years and shared with Division staff on request on `live_virtual_training_procedures.md` lines 35-36.
- The procedures require DCJS sign-in sheet completion, ID confirmation, and `COC` entry on `live_virtual_training_procedures.md` lines 37-38 and 51.
- The procedures require students and instructor to be visible on camera during live instruction on `live_virtual_training_procedures.md` lines 39-42.
- The procedures limit prerecorded content and prohibit replaying recorded classes instead of live instruction on `live_virtual_training_procedures.md` lines 43-45.
- The procedures require Acadis Portal reporting with `online training` after the instructor name and in the comment section on `live_virtual_training_procedures.md` lines 47-51.

## What We Are Not Building Yet

These should not be part of the first MVP unless absolutely necessary:

- A full prerecorded LMS course library.
- Automatic certificate release without attendance review.
- Complex recurring subscriptions.
- Complex time-slot booking by hour.
- A custom video meeting system built inside the website.

Proof:

- The meeting separates this from an LMS-style prerecorded course system on lines 1647-1663.
- It says the training is live, not prerecorded LMS training, on lines 1929-1939.
- It says the class is by day, not by time, on lines 1761-1786.
- It says payment is one-time per class on lines 2592-2611.

## Simple User Flow

1. Student visits the training website.
2. Student reviews programs, prices, and requirements.
3. Student selects a class day.
4. Student creates an account or enters registration details.
5. Student pays one time for the selected class.
6. Student receives a meeting URL/code by email.
7. Student joins the live class at the fixed time.
8. Instructor verifies attendance and camera participation.
9. Student takes the simple online test.
10. Admin/instructor confirms completion.
11. Certificate is generated and emailed or made available for download.

## MVP Priority List

Build in this order:

1. Training website pages: Home, About, Programs, Enrollment, Pricing, Contact, FAQ.
2. Class schedule and day-based booking.
3. Student registration and one-time payment.
4. Email delivery of meeting link/code.
5. Attendance tracking process.
6. Recording and storage process.
7. Simple test flow.
8. Certificate template and completion-based certificate release.
9. Compliance/admin layer for DCJS approval tracking, announcements, COC roster, ID verification, forms, audit links, and Acadis reporting support.

## Main Assumptions

- Start with online/live training first because in-person training has room costs.
- Use Zoom, Google Meet, Teams, or WebEx instead of building custom video hosting.
- Keep certificates controlled by attendance/completion, not just payment.
- Use a simple website plus live meeting tools for MVP instead of a full LMS.
- Link the training website from the existing Utica Security Services website, but keep Utica Security Training as its own training brand/domain.
